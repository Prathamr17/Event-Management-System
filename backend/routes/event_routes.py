from flask import Blueprint, request, jsonify
from models.event import Event
from extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

event_bp = Blueprint("events", __name__)

@event_bp.route("/", methods=["POST"])
@jwt_required()
def create_event():
    data = request.get_json()
    user_id = int(get_jwt_identity())

    event = Event(
        title=data["title"],
        description=data.get("description", ""),
        location=data["location"],
        date=datetime.strptime(data["date"], "%Y-%m-%d").date(),
        created_by=user_id
    )

    db.session.add(event)
    db.session.commit()

    return jsonify(message="Event created"), 201



@event_bp.route("/", methods=["GET"])
@jwt_required()
def get_events():
    user_id = int(get_jwt_identity())

    events = Event.query.filter_by(created_by=user_id).all()

    return jsonify([
        {
            "id": e.id,
            "title": e.title,
            "description": e.description,
            "location": e.location,
            "date": e.date.isoformat()
        }
        for e in events
    ]), 200


@event_bp.route("/<int:event_id>", methods=["DELETE"])
@jwt_required()
def delete_event(event_id):
    user_id = int(get_jwt_identity())

    event = Event.query.filter_by(id=event_id, created_by=user_id).first_or_404()

    db.session.delete(event)
    db.session.commit()

    return jsonify(message="Event deleted"), 200


@event_bp.route("/<int:event_id>", methods=["PUT"])
@jwt_required()
def update_event(event_id):
    user_id = int(get_jwt_identity())
    data = request.get_json()

    event = Event.query.filter_by(
        id=event_id,
        created_by=user_id
    ).first_or_404()

    event.title = data.get("title", event.title)
    event.description = data.get("description", event.description)
    event.location = data.get("location", event.location)
    event.date = datetime.strptime(
        data.get("date", event.date.strftime("%Y-%m-%d")),
        "%Y-%m-%d"
    )

    db.session.commit()

    return jsonify(message="Event updated successfully"), 200
