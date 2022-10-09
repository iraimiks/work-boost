from flaskr import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    user_role = db.Column(db.String(length=30))
    name = db.Column(db.String(length=30))
    username = db.Column(db.String(length=30))
    password = db.Column(db.String(128))
    phone = db.Column(db.String(length=30))
    create_date = db.Column(db.DateTime)
    def __init__(self, user_role, name, username, password, phone, create_date):
        self.user_role = user_role
        self.name = name
        self.username = username
        self.phone = phone
        self.password = generate_password_hash(password)
        self.create_date = create_date
    @property
    def serialized(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'phone': self.phone,
            'user_role': self.user_role,
            'create_date': self.create_date
        }
