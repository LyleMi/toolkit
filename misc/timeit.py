#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import subprocess


def count(args):
    start_time = time.perf_counter()
    process = subprocess.Popen(args)
    process.wait()
    stop_time = time.perf_counter()
    cost = stop_time - start_time
    # print(cost)
    return cost


def main():
    # print(sys.argv[1:])
    times = int(sys.argv[1])
    costs = []
    for i in range(times):
        print('run %s' % i, end='\r')
        costs.append(count(sys.argv[2:]))
    total = sum(costs)
    average = total / times
    print(
        'run %s times, average %s, total %s' % (
            times,
            average,
            total
        )
    )


if __name__ == '__main__':
    main()
