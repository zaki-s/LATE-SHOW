from flask import Flask
from flask_jwt_extended import JWTManager
from server.extensions import db, migrate
from server.config import Config
from server.routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    JWTManager(app)

    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
