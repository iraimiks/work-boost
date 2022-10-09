import functools
import datetime

from flask import (
    Blueprint, g, request, session, jsonify
)
from flaskr import db

from flaskr.users.user import User


bp = Blueprint('auth', __name__, url_prefix='/auth')

def logged_in(f):
    @functools.wraps(f)
    def decorated_func(*args, **kwargs):
        if session.get('username'):
            return f(*args, **kwargs)
        else:
            return jsonify(status='logout')
    return decorated_func


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        json_data = request.get_json()
        username = json_data['username']
        user = User.query.filter_by(username=username).first()
        message = ''
        if user is None:
            message = 'Incorect Username'
            return jsonify(username=str(username), message=message)
        else:
            session['username'] = user.username
            return jsonify(status='logined', id=user.id)

@bp.before_app_request
def load_logged_in_user():
    username = session.get('username')
    if username is None:
        g.username = None
    else:
        g.username = User.query.filter_by(username=username).first()

@bp.route('/logout')
@logged_in
def logout():
    session.clear()
    return jsonify(status='logout')

@bp.route('/reg_worker', methods=('GET', 'POST'))
def worker_reg():
    if request.method == 'POST':
        json_data = request.get_json()
        name = json_data['name']
        username = json_data['username']
        password  = json_data['password']
        phone = json_data['phone']
        role = 'worker'
        new_worker = User(role, name, username, password, phone, create_date=datetime.datetime.now())
        db.session.add(new_worker)
        db.session.commit()
        return jsonify(status="register")