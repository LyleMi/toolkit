#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""Database Wrapper for mongodb client
"""

from pymongo import MongoClient


class Mongo(object):

    """
    MongoDB Client
    
    Attributes:
        col (object): mongo.database.collection
        conn (object): database connection
        db (object): mongo.database
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
            user (None, optional): username
            pwd (None, optional): password
        """
        super(Mongo, self).__init__()
        self.conn = MongoClient(ip, port)
        if user is not None and pwd is not None:
            self.conn.authenticate(user, pwd)
        self.db = self.conn[db]
        self.col = self.db[collection]

    def insert(self, data):
        """
        Auto use insert_one or insert_many to insert
        depends on data's type
        
        Args:
            data (dict or list): data to insert
        """
        if isinstance(data, dict):
            self.col.insert_one(data)
        elif isinstance(data, list):
            self.col.insert_many(data)

    def find(self, index={}):
        """find data
        
        Args:
            index (dict, optional): Description
        
        Returns:
            list: data
        """
        return [i for i in self.col.find(index)]

    def update(self, condition, data, many=True):
        """Update
        
        Args:
            condition (dict): update condition
            data (dict): update data
            many (bool, optional): update one or many
        """
        if many:
            self.col.update_many(condition, data)
        else:
            self.col.update_one(condition, data)

    def delete(self, condition={}, many=True):
        """delete
        
        Args:
            condition (dict, optional): delete condition
            many (bool, optional): delete one or many
        """
        if many:
            self.col.delete_many(condition)
        else:
            self.col.delete_one(condition)

    def switchDB(self, db):
        """switch Database
        
        Args:
            db (str): switch db
        """
        self.db = self.conn[db]

    def switchCol(self, col):
        """switch collection
        
        Args:
            col (str): switch collection
        """
        self.col = self.db[col]

    def drop(self):
        """drop collection
        """
        self.col.drop()

if __name__ == '__main__':
    m = Mongo('test', 'test')
    m.insert({'datajson': 'test'})
    print(m.find({}))
    m.delete()
    print(m.find())
