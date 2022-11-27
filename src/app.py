from flask import Flask
from controllers.hello_controller import hello_controller
from database import db
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

def create_app():
    app = Flask(__name__)

    app.register_blueprint(hello_controller)

    # Fix the URI for Fly configuration
    database_uri = os.getenv("DATABASE_URL")
    database_uri = database_uri.replace("postgres://", "postgresql://")
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

    db.init_app(app)

    return app