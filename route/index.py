from flask import Blueprint, redirect, url_for

index_bp = Blueprint("index", __name__)


@index_bp.route("/")
def index():
    return "hello world"


@index_bp.route("/save_emails")
def redirect_and_save_emails():
    return redirect(url_for("event_mail.save_emails"))
