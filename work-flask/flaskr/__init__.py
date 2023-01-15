import config
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = config.sqlcon
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.secret_key = config.appsecret
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

from flaskr import auth, manage

app.register_blueprint(auth.bp)
app.register_blueprint(manage.bp)