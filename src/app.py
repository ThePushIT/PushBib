from flask import Flask
from controllers.hello_controller import hello_controller

app = Flask(__name__)

def create_app():
    app = Flask(__name__)

    app.register_blueprint(hello_controller)

    return app