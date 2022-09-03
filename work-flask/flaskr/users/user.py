import imp
from flaskr import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_role = db.Column(db.String(length=30))
    username = db.Column(db.String(length=30))
    password = db.Column(db.String(128))
    def __init__(self, user_role, username, password):
        self.user_role = user_role
        self.username = username
        self.password = generate_password_hash(password)