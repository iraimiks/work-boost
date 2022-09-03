import config
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = config.sqlcon
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.secret_key = config.appsecret
db = SQLAlchemy(app)
CORS(app)

from flaskr import route, auth

app.register_blueprint(auth.bp)
