from flask import Blueprint, request, jsonify
from server.models import Guest
from server.extensions import db

guests_bp = Blueprint("guests", __name__)

@guests_bp.route("/guests", methods=["POST"])
def create_guest():
    data = request.get_json()
    name = data.get("name")
    occupation = data.get("occupation")

    if not name or not occupation:
        return jsonify({"error": "Name and occupation required"}), 400

    guest = Guest(name=name, occupation=occupation)
    db.session.add(guest)
    db.session.commit()

    return jsonify({
        "message": "Guest added",
        "guest": {
            "id": guest.id,
            "name": guest.name,
            "occupation": guest.occupation
        }
    }), 201
