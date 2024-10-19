from flask import Blueprint,request,jsonify
from .db import get_db, check_mongo_connection
import logging

logger=logging.getLogger(__name__)

main= Blueprint('main',__name__)
db= get_db()
users_collection=db['users']

@main.route('/')
def hello_world():
    return 'Hello, World!'


@main.route('/add_user',methods=['POST'])
def create_user():
    data=request.get_json()
    usename=data.get('username')
    password=data.get('password')
    email=data.get('email')
    if usename and password and email:
        
        users_collection.insert_one({'username':usename,'password':password, 'email':email})
        return jsonify({'message':'user created successfully'}), 201

    else:
        return jsonify({'message':'user not created'}), 400

@main.route('/get_users', methods=['GET'])
def get_users():
    users_list = list(users_collection.find({}, {'_id': 0}))
    logger.info("Fetched users list")
    return jsonify(users_list), 200

