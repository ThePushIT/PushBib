from flask import Blueprint, render_template

hello_controller = Blueprint("hello", __name__)

@hello_controller.route('/')
def hello():
    return render_template("index.html")
