from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from PragmatechApp.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    from PragmatechApp.admin.routes import admin
    from PragmatechApp.user.routes import user

    app.register_blueprint(admin)
    app.register_blueprint(user)

    return app