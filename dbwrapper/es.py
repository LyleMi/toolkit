#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Elastic Search Database Client wrapper class
"""

import elasticsearch


class ElasticSearchDB(object):

    """Elastic Search Database Client wrapper

    Attributes:
        client (obj): ElasticSearchDB client
        doctype (str): default doc type
        index (str): default index
    """

    def __init__(self, servers, index, doctype):
        """init param

        Args:
            servers (list): Elastic Search Database Server Info
            index (str): default index
            doctype (str): default doc type
        """
        self.client = elasticsearch.Elasticsearch(hosts=es_servers)
        self.index = index
        self.doctype = doctype

    def add(self, sid, row):
        """add some data

        Args:
            sid (str): data id
            row (dict): data to be added
        """
        self.client.index(
            index=self.index,
            doc_type=self.doctype,
            body=row,
            id=sid
        )

    def search(self, row):
        """search data

        Args:
            row (dict): search definition using the Query DSL 

        Returns:
            dict: search data
        """
        return self.client.search(
            index=self.index,
            doc_type=self.doctype,
            body=row
        )

    def update(self, sid, row_obj):
        """update data

        Args:
            sid (str): data id
            row_obj (dict): data to be added
        """
        self.client.update(
            index=self.index,
            doc_type=self.doctype,
            body={"doc": row_obj},
            id=sid
        )

    def delete(self, sid=None, row=None):
        """delete data, if sid is given, use sid, else use row to search and delete

        Args:
            sid (str): data id
            row (dict, optional): search definition using the Query DSL 
        """
        if sid is not None:
            self.client.delete(
                index=self.index,
                doc_type=self.doctype,
                id=sid
            )
        elif row is not None:
            self.client.delete_by_query(
                index=self.index,
                doc_type=self.doctype,
                body=row
            )


if __name__ == '__main__':
    servers = [{
        "host": "localhost",
        "port": "9200"
    }]
    es = ElasticSearchDB(servers, "ind", "dtype")
