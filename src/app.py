from flask import Flask
from controllers.user_controller import user_controller
from controllers.references_controller import ref_controller
from controllers.test_controller import test_controller
from controllers.language_controller import language_controller
from database import db
from config import DATABASE_URL, ENV, SECRET_KEY
from flask_babel import Babel


def create_app():
    app = Flask(__name__)

    app.register_blueprint(user_controller)
    app.register_blueprint(ref_controller)
    app.register_blueprint(language_controller)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["BABEL_TRANSLATION_DIRECTORIES"] = './../translations'
    app.secret_key = SECRET_KEY

    if ENV == "development":
        app.register_blueprint(test_controller)

    db.init_app(app)
    babel = Babel(app)

    return app
