from flask import Blueprint, jsonify
from models.event import Event

report_bp = Blueprint("reports", __name__)

@report_bp.route("/summary", methods=["GET"])
def report():
    events = Event.query.count()
    return jsonify(total_events=events)
