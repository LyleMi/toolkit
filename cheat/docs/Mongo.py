from docs.base import Base


class Mongo(Base):

    _doc = {
        "auth": """
use admin
db.auth("username", "password")
db.auth("root", passwordPrompt())
""",
        "db": """
show dbs
use db_name
""",
        "collection": """
show collections
db.createCollection(name, options)
db.collection_name.drop()

db.collection_name.insert(document)
db.collection_name.insertOne(...)
db.collection_name.insertMany(...)
db.collection_name.save(document)
db.collection_name.update(...)
db.collection_name.remove(...)
db.collection_name.find(...)
db.collection_name.findOne(...)
""",
    }
