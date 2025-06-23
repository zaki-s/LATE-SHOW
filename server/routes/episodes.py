from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models import Episode
from server.extensions import db
from datetime import datetime

episodes_bp = Blueprint("episodes", __name__)

@episodes_bp.route("/episodes", methods=["POST"])
@jwt_required()
def create_episode():
    data = request.get_json() or {}
    date_str = data.get("date")
    number = data.get("number")

    if not isinstance(date_str, str) or not isinstance(number, int):
        return jsonify({"error": "Invalid or missing 'date' (string) and 'number' (integer)"}), 400

    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

    episode = Episode(date=date_obj, number=number)
    db.session.add(episode)
    db.session.commit()

    return jsonify({
        "message": "Episode created",
        "episode": {
            "id": episode.id,
            "date": episode.date.isoformat(),
            "number": episode.number
        }
    }), 201

@episodes_bp.route("/episodes", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([
        {
            "id": ep.id,
            "date": ep.date.isoformat(),
            "number": ep.number
        } for ep in episodes
    ])

@episodes_bp.route("/episodes/<int:id>", methods=["GET"])
def get_single_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    return jsonify({
        "id": episode.id,
        "date": episode.date.isoformat(),
        "number": episode.number
    })
