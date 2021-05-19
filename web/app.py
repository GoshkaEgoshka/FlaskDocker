"""
    Endpoints
"""
import json
from flask import request

from init import create_app
from database import add_user_to_db, get_users, get_user_by_id, remove, update_user

app = create_app()


@app.route('/')
def index():
    """
        Main page
    """
    return 'Flask app'


@app.route('/users', methods=['GET'])
def show_users():
    """
        Shows all users
    """
    all_users = get_users()
    return json.dumps(all_users), 200


@app.route('/add_user', methods=['POST'])
def add_user():
    """
        Add user
    """
    data = request.get_json()
    user_id = data['id']
    username = data['username']
    email = data['email']
    add_user_to_db(user_id=user_id, username=username, email=email)
    return json.dumps('Added'), 200


@app.route('/<user_id>', methods=['GET', 'DELETE', 'PUT'])
def read_update_delete_user_by_id(user_id):
    """
        Reads, Updates, Deletes user
    """
    if request.method == 'PUT':
        data = request.get_json()
        new_username = data['username']
        new_email = data['email']
        result = update_user(user_id=user_id, username=new_username, email=new_email)
    elif request.method == 'GET':
        result = get_user_by_id(user_id)
    elif request.method == 'DELETE':
        result = remove(user_id)
    return json.dumps(result), 200
