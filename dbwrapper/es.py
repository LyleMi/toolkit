#!/usr/bin/env python
# -*- coding: utf-8 -*-

import elasticsearch


class ElasticSearchDB(object):

    def __init__(self, servers, index, doctype):
        self.client = elasticsearch.Elasticsearch(hosts=es_servers)
        self.index = index
        self.doctype = doctype

    def add(self, sid, row):
        self.client.index(
            index=self.index,
            doc_type=self.doctype,
            body=row,
            id=sid
        )

    def search(self, row):
        return self.client.search(
            index=self.index,
            doc_type=self.doctype,
            body=row
        )

    def update(self, sid, row):
        self.client.update(
            index=self.index,
            doc_type=self.doctype,
            body={"doc": row_obj},
            id=sid
        )

    def delete(self, sid):
        self.client.delete(
            index=self.index,
            doc_type=self.doctype,
            id=sid
        )


if __name__ == '__main__':
    servers = [{
        "host": "localhost",
        "port": "9200"
    }]
    es = ElasticSearchDB(servers, "ind", "dtype")
