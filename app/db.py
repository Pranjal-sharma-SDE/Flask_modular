from pymongo import MongoClient
import os
import logging

# intialize logger
logger=logging.getLogger(__name__)


def get_db():
    client = MongoClient(os.getenv('MONGODB_URI'))
    db = client.get_default_database()
    return db


def check_mongo_connection():
    """ Ping MongoDB to check connection """

    try:
        client = MongoClient(os.getenv('MONGODB_URI'))
        client.admin.command('ping')
        logger.info("MongoDB connected")
        return True
    except Exception as e:
        logger.error(f"MongoDB connection error: {e}", exc_info=True)
        return False

