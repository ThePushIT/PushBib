from flask import Blueprint

hello_controller = Blueprint("hello", __name__)

@hello_controller.route('/')
def hello():
    return "Hello World!"
