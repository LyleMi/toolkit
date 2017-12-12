#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient


class Mongo(object):

    """
    MongoDB Client
    """

    def __init__(self, db, collection,
                 ip="localhost", port=27017,
                 user=None, pwd=None):
        """
        Args:
            db (str): db to use
            collection (str): collection to use
            ip (str, optional): dbtabase ip
            port (int, optional): dbtabase port
        """
        super(Mongo, self).__init__()
        self.conn = MongoClient(ip, port)
        if user is not None and pwd is not None:
            self.conn.authenticate(user, pwd)
        self.col = self.conn[db][collection]

    def insert(self, data):
        self.col.insert(data)

    def find(self, index={}):
        return [i for i in self.col.find(index)]

    def delete(self, index={}):
        self.col.remove(index)

if __name__ == '__main__':
    m = Mongo('test', 'test')
    m.insert({'datajson': 'test'})
    print m.find({})
    m.delete()
    print m.find()
