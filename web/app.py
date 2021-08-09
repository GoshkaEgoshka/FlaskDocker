"""
    Endpoints
"""
import json

from flask import request, Flask, render_template, redirect, url_for, session, flash
from flask_migrate import Migrate
from web.models import db, Users
from web.database import (
    add_user_to_db, get_users,
    get_user_by_id, remove_user,
    update_user
)
from web.validation import UserValidation
from web.login_helper import login_check

app = Flask(__name__, template_folder='templates')
app.config.from_pyfile('config.py')
app.secret_key = 'super_secret'
db.init_app(app)
migrate = Migrate(app, db)

user_validation = UserValidation()
   

@app.route('/')
@login_check
async def index():
    """
        Main page
    """
    return render_template('index.html', email=session['email'])


@app.route('/login',  methods=['POST'])
async def post_authorization():
    """
        Post method authorization
    """
    email = request.form.get('email')

    user = Users.query.filter_by(email=email).first()
    if user:
        session['email'] = email
        session['login'] = True
        return redirect(url_for('index'))
    flash('Your email is wrong. Try again.')
    return render_template('authorization.html')


@app.route('/login',  methods=['GET'])
async def get_authorization():
    """
        Post method authorization
    """
    return render_template('authorization.html')


@app.route('/users', methods=['GET'])
async def show_users():
    """
        Shows all users
    """
    all_users = await get_users()
    return json.dumps(all_users), 200


@app.route('/add_user', methods=['POST'])
async def add_user():
    """
        Add user
    """
    data = request.get_json()
    errors = user_validation.validate(data)
    if errors:
        return json.dumps('User parameters are not valid'), 400
    user_id = data['id']
    username = data['username']
    email = data['email']
    await add_user_to_db(user_id=user_id, username=username, email=email)
    return json.dumps('Added'), 200


@app.route('/<int:user_id>', methods=['GET', 'DELETE', 'PUT'])
async def read_update_delete_user_by_id(user_id):
    """
        Reads, Updates, Deletes user
    """
    if request.method == 'PUT':
        data = request.get_json()
        errors = user_validation.validate(data)
        if errors:
            return json.dumps('User parameters are not valid'), 400
        new_username = data['username']
        new_email = data['email']
        result = await update_user(
            id=user_id, username=new_username, email=new_email
        )
    elif request.method == 'GET':
        result = await get_user_by_id(id=user_id)
    elif request.method == 'DELETE':
        result = await remove_user(id=user_id)
    return json.dumps(result), 200
