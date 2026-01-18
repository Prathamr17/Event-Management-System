from flask import Blueprint, request, jsonify
from models.feedback import Feedback
from extensions import db

feedback_bp = Blueprint("feedback", __name__)

@feedback_bp.route("/", methods=["POST"])
def submit_feedback():
    fb = Feedback(**request.json)
    db.session.add(fb)
    db.session.commit()
    return jsonify(message="Feedback recorded")
