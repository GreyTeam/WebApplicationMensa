import pymongo
import os

db = pymongo.MongoClient("mongodb://mensa-admin:mensa!!123@localhost:27017/")["mensa"]

def get_db():
    return db