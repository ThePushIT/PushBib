import os
from os import getenv
from flask import Flask
from dotenv import load_dotenv
from controllers.hello_controller import hello_controller
from controllers.user_controller import user_controller
from controllers.references_controller import ref_controller
from database import db


app = Flask(__name__)
load_dotenv()
app.secret_key = getenv("SECRET_KEY")


def create_app():
    app.register_blueprint(hello_controller)
    app.register_blueprint(user_controller)
    app.register_blueprint(ref_controller)

    # Fix the URI for Fly configuration
    database_uri = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

    db.init_app(app)

    return app
