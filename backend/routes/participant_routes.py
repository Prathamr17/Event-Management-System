from flask import Blueprint, request, jsonify
from models.participant import Participant
from extensions import db

participant_bp = Blueprint("participants", __name__)

@participant_bp.route("/", methods=["POST"])
def add_participant():
    p = Participant(**request.json)
    db.session.add(p)
    db.session.commit()
    return jsonify(message="Participant added")
