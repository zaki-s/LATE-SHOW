from flask import Flask
from flask_jwt_extended import JWTManager
from .models import db, migrate
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    JWTManager(app)

    return app