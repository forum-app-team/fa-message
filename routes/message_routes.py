from flask import Blueprint
from controllers.message_controller import (
    get_all_messages,
    get_message_by_id,
    send_message,
)

message_bp = Blueprint("message_bp", __name__)


@message_bp.route("/api/messages", methods=["GET"])
def get_messages():
    return get_all_messages()


@message_bp.route("/api/messages/<int:id>", methods=["GET"])
def get_message(id):
    return get_message_by_id(id)


@message_bp.route("/api/messages", methods=["POST"])
def user_send_message():
    return send_message()
