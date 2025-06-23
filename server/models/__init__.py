from server.extensions import db
from .user import User
from .guest import Guest
from .episode import Episode
from .appearance import Appearance
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate\


db = SQLAlchemy()
migrate = Migrate()