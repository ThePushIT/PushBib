from flask import Blueprint, render_template, redirect

from services.user_service import user_service

hello_controller = Blueprint("hello", __name__)


@hello_controller.route('/')
def hello():
    user_id = user_service.get_id()

    if user_id!=0:
        return redirect('/references')

    return render_template("index.html")
