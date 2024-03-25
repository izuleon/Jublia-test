from datetime import datetime

import pytz
from flask import Blueprint, abort, jsonify, request

recipient_bp = Blueprint("recipient", __name__, url_prefix="/recipient")

from usecase import recipient


@recipient_bp.get("/")
def get_distinct_event_id():
    result = recipient.get_all_event_id_registered_to_recipient()
    return jsonify(result)


@recipient_bp.get("/event/<int:event_id>")
def get_recipient_in_event(event_id: int):
    result = recipient.get_all_recipient_by_event_id(event_id)
    return jsonify(result)


@recipient_bp.get("/id/<int:id>")
def get_recipient_by_id(id: int):
    result = recipient.get_recipient_by_id(id)
    if result == None:
        return jsonify({"error": "Recipient not found"}), 404
    return jsonify(result)


@recipient_bp.post("/")
def save_emails():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing data in request body"}), 400

    # Extract data from request
    event_id = data.get("event_id")
    email_recipient = data.get("email_recipient")

    result = recipient.save_recipient(
        event_id=event_id,
        email_recipient=email_recipient,
    )
    return result
