from flask import Blueprint, request, jsonify
from server.models import Appearance
from server.extensions import db

appearances_bp = Blueprint("appearances", __name__)

@appearances_bp.route("/appearances", methods=["POST"])
def create_appearance():
    data = request.get_json()
    guest_id = data.get("guest_id")
    episode_id = data.get("episode_id")
    rating = data.get("rating")

    if not all([guest_id, episode_id, rating]):
        return jsonify({"error": "guest_id, episode_id, and rating required"}), 400

    appearance = Appearance(guest_id=guest_id, episode_id=episode_id, rating=rating)
    db.session.add(appearance)
    db.session.commit()

    return jsonify({
        "message": "Appearance recorded",
        "appearance": {
            "id": appearance.id,
            "guest_id": appearance.guest_id,
            "episode_id": appearance.episode_id,
            "rating": appearance.rating
        }
    }), 201
