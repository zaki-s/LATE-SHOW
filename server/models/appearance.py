from sqlalchemy.orm import validates
from server.extensions import db

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id', ondelete='CASCADE'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id', ondelete='CASCADE'), nullable=False)

    guest = db.relationship('Guest', back_populates='appearances', lazy='joined')
    episode = db.relationship('Episode', back_populates='appearances', lazy='joined')

    @validates('rating')
    def validate_rating(self, key, value):
        if not isinstance(value, int) or not 1 <= value <= 5:
            raise ValueError("Rating must be an integer between 1 and 5")
        return value
