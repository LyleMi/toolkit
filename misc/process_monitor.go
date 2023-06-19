package main

import (
    "flag"
    "fmt"
    "log"
    "time"
    "net/http"
    "os"

    "github.com/prometheus/client_golang/prometheus"
    "github.com/prometheus/client_golang/prometheus/promhttp"
    "github.com/shirou/gopsutil/process"
    "github.com/shirou/gopsutil/net"
)

var (
    addr        = flag.String("listen-address", ":8080", "The address to listen on for HTTP requests.")
    processName = flag.String("process-name", "", "The name of the process to monitor.")
    interval    = flag.Duration("interval", 10*time.Second, "The interval between metric collection.")
)

type processCollector struct {
    cpu    *prometheus.Desc
    memory *prometheus.Desc
    netIO  *prometheus.Desc
    diskIO *prometheus.Desc
    netIORate  *prometheus.Desc
    diskIORate *prometheus.Desc
}

func newProcessCollector() *processCollector {
    return &processCollector{
        cpu: prometheus.NewDesc("process_cpu_percent",
            "CPU percentage used by the process",
            nil, nil,
        ),
        memory: prometheus.NewDesc("process_memory_percent",
            "Memory percentage used by the process",
            nil, nil,
        ),
        netIO: prometheus.NewDesc("process_net_io",
            "Network IO used by the process",
            []string{"direction"}, nil,
        ),
        diskIO: prometheus.NewDesc("process_disk_io",
            "Disk IO used by the process",
            []string{"direction"}, nil,
        ),
        netIORate: prometheus.NewDesc("process_net_io_rate",
            "Network IO rate used by the process",
            []string{"direction"}, nil,
        ),
        diskIORate: prometheus.NewDesc("process_disk_io_rate",
            "Disk IO rate used by the process",
            []string{"direction"}, nil,
        ),
    }
}

var (
    lastNetIO  *net.IOCountersStat
    lastDiskIO *process.IOCountersStat
    lastTime   time.Time
)

func (c *processCollector) Describe(ch chan<- *prometheus.Desc) {
    ch <- c.cpu
    ch <- c.memory
    ch <- c.netIO
    ch <- c.diskIO
    ch <- c.netIORate
    ch <- c.diskIORate
}

func (c *processCollector) Collect(ch chan<- prometheus.Metric) {
    proc, err := findProcessByName(*processName)
    if err != nil {
        log.Printf("Error finding process: %v", err)
        return
    }

    cpuPercent, _ := proc.CPUPercent()
    ch <- prometheus.MustNewConstMetric(c.cpu, prometheus.GaugeValue, cpuPercent)

    memPercent, _ := proc.MemoryPercent()
    ch <- prometheus.MustNewConstMetric(c.memory, prometheus.GaugeValue, float64(memPercent))

    netIOCounters, _ := proc.NetIOCounters(false)
    for _, netIO := range netIOCounters {
        ch <- prometheus.MustNewConstMetric(c.netIO, prometheus.CounterValue, float64(netIO.BytesSent), "sent")
        ch <- prometheus.MustNewConstMetric(c.netIO, prometheus.CounterValue, float64(netIO.BytesRecv), "received")
    }

    ioCounters, err := proc.IOCounters()
    if err != nil {
        log.Printf("Error get ioCounters: %v", err)
        return
    }
    ch <- prometheus.MustNewConstMetric(c.diskIO, prometheus.CounterValue, float64(ioCounters.ReadBytes), "read")
    ch <- prometheus.MustNewConstMetric(c.diskIO, prometheus.CounterValue, float64(ioCounters.WriteBytes), "write")

    now := time.Now()
    if lastNetIO != nil && lastDiskIO != nil {
        duration := now.Sub(lastTime).Seconds()

        netSentRate := (float64(netIOCounters[0].BytesSent) - float64(lastNetIO.BytesSent)) / duration
        netRecvRate := (float64(netIOCounters[0].BytesRecv) - float64(lastNetIO.BytesRecv)) / duration
        ch <- prometheus.MustNewConstMetric(c.netIORate, prometheus.GaugeValue, netSentRate, "sent")
        ch <- prometheus.MustNewConstMetric(c.netIORate, prometheus.GaugeValue, netRecvRate, "received")

        diskReadRate := (float64(ioCounters.ReadBytes) - float64(lastDiskIO.ReadBytes)) / duration
        diskWriteRate := (float64(ioCounters.WriteBytes) - float64(lastDiskIO.WriteBytes)) / duration
        ch <- prometheus.MustNewConstMetric(c.diskIORate, prometheus.GaugeValue, diskReadRate, "read")
        ch <- prometheus.MustNewConstMetric(c.diskIORate, prometheus.GaugeValue, diskWriteRate, "write")
    }

    lastNetIO = &netIOCounters[0]
    lastDiskIO = ioCounters
    lastTime = now
}

func findProcessByName(name string) (*process.Process, error) {
    processes, err := process.Processes()
    if err != nil {
        return nil, err
    }

    for _, p := range processes {
        pName, _ := p.Name()
        if pName == name {
            return p, nil
        }
    }

    return nil, fmt.Errorf("process not found: %s", name)
}

func main() {
    flag.Parse()

    if *processName == "" {
        fmt.Println("Please provide a process name using the -process-name flag.")
        os.Exit(1)
    }

    collector := newProcessCollector()
    prometheus.MustRegister(collector)

    go func() {
        for range time.Tick(*interval) {
            collector.Collect(make(chan prometheus.Metric))
        }
    }()

    http.Handle("/metrics", promhttp.Handler())
    log.Printf("Starting server on %s, monitoring process: %s", *addr, *processName)
    log.Fatal(http.ListenAndServe(*addr, nil))
}
