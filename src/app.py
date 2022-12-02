import os
from os import getenv
from flask import Flask
from dotenv import load_dotenv
from controllers.hello_controller import hello_controller
from controllers.user_controller import user_controller
from controllers.references_controller import ref_controller
from controllers.test_controller import test_controller
from database import db


app = Flask(__name__, template_folder='templates')
load_dotenv()
app.secret_key = getenv("SECRET_KEY")


ENV = os.getenv("FLASK_ENV") or 'production'
print('env', ENV)

def create_app():
    app.register_blueprint(hello_controller)
    app.register_blueprint(user_controller)
    app.register_blueprint(ref_controller)

    # Fix the URI for Fly configuration
    database_uri = os.getenv("DATABASE_URL")
    database_uri = database_uri.replace("postgres://", "postgresql://")
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

    if ENV == "development":
        app.register_blueprint(test_controller)

    db.init_app(app)

    return app