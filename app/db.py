from pymongo import MongoClient
import os
import logging

# intialize logger
logger=logging.getLogger(__name__)


def get_db():
    client = MongoClient(os.getenv('MONGO_URI'))
    db = client['user_database'] 

    # check if database exists
    check_mongo_connection()
    if check_mongo_connection():
        logger.info('Connected to MongoDB')
    return db


def check_mongo_connection():
    """ Ping MongoDB to check connection """

    try:
        client = MongoClient(os.getenv('MONGO_URI'))
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
        logger.error("Failed to connect to MongoDB")

