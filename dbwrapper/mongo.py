#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient


class Mongo(object):

    """
    MongoDB Client
    """

    def __init__(self, db, collection):
        super(Mongo, self).__init__()
        self.conn = MongoClient('localhost')
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
