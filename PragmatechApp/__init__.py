from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f59c3b6c7cb1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from PragmatechApp.admin.routes import admin
from PragmatechApp.user.routes import user

app.register_blueprint(admin)
app.register_blueprint(user)