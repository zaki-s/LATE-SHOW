from flask import Flask
from flask_jwt_extended import JWTManager
from server.models import User, Guest, Episode, Appearance
from server.extensions import db, migrate
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    JWTManager(app)

    # Import models so Flask-Migrate can register them
    with app.app_context():
        from server import models

    return app
