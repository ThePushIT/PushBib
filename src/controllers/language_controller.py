from flask import Blueprint, redirect
import flask_babel
from services.language_service import language_service

language_controller = Blueprint("lang", __name__)

@language_controller.route("/language/<lang>", methods=["POST", "GET"])
def set_language(lang):
    language_service.set_language(lang)
    flask_babel.refresh()
    return redirect("/")
