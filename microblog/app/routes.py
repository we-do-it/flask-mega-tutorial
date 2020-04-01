import json
from app import app, db
from app.models import User
from flask import jsonify, Response

@app.route('/')
@app.route('/index')
def index():
    user = { 'username': 'joske' }
    return jsonify(user)

@app.route('/seed')
def seed():
    u = User(username='joske2', email='joske@cl21.be', password_hash='123')
    db.session.add(u)
    db.session.commit()
    return 'ok'

@app.route('/users')
def users():
    users = User.query.all()
    # not really what we want for now but sufficient to test our db querying
    # we will use a list in the future
    result = {}
    i = 0
    for user in users:
        result['user' + str(i)] = user.username
        result['email' + str(i)] = user.email
        i = i + 1

    return result
