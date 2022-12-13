from flask import Blueprint, redirect
import flask_babel
from services.language_service import language_service

language_controller = Blueprint("lang", __name__)

@language_controller.route("/language/<lang>/<page>", methods=["POST", "GET"])
def set_language(lang, page):
    language_service.set_language(lang)
    flask_babel.refresh()
    path = "/"
    if page == "signup":
        path = "/signup"
    elif page == "references":
        path = "/references"

    return redirect(path)
