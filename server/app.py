from flask import Flask
from flask_jwt_extended import JWTManager
from server.extensions import db, migrate
from server.config import Config
from server.routes import auth_bp, episodes_bp, guests_bp, appearances_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    JWTManager(app)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(episodes_bp)
    app.register_blueprint(guests_bp)
    app.register_blueprint(appearances_bp)

    return app
