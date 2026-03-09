from flask import Blueprint, request, jsonify
from ..models import Event, Registration
from .. import db

events_bp = Blueprint("events", __name__)

@events_bp.route("/events", methods=["POST"])
def create_event():

    data = request.json

    event = Event(
        name=data["name"],
        total_seats=data["total_seats"],
        available_seats=data["total_seats"]
    )

    db.session.add(event)
    db.session.commit()

    return jsonify({"message": "Event created"})


@events_bp.route("/events", methods=["GET"])
def list_events():

    events = Event.query.all()

    result = []

    for e in events:
        result.append({
            "id": e.id,
            "name": e.name,
            "total_seats": e.total_seats,
            "available_seats": e.available_seats
        })

    return jsonify(result)


@events_bp.route("/register/<int:event_id>", methods=["POST"])
def register_user(event_id):

    data = request.json

    event = Event.query.get(event_id)

    if not event:
        return jsonify({"error": "Event not found"})

    if event.available_seats == 0:
        return jsonify({"message": "Registration failed. No seats available."})

    registration = Registration(
        user_name=data["user_name"],
        event_id=event_id
    )

    event.available_seats -= 1

    db.session.add(registration)
    db.session.commit()

    return jsonify({"message": "User registered successfully"})

@events_bp.route("/events/full")
def full_events():

    events = Event.query.filter_by(available_seats=0).all()

    result = []

    for e in events:
        result.append({
            "id": e.id,
            "name": e.name
        })

    return jsonify(result)