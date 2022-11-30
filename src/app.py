import os
from flask import Flask
from dotenv import load_dotenv
from controllers.hello_controller import hello_controller
<<<<<<< HEAD
from controllers.user_controller import user_controller
=======
from controllers.references_controller import ref_controller
>>>>>>> 3f723775cc55555e43504763b467e804a6956082
from database import db


app = Flask(__name__)
load_dotenv()

def create_app():
    app.register_blueprint(hello_controller)
<<<<<<< HEAD
    app.register_blueprint(user_controller)
=======
    app.register_blueprint(ref_controller)
>>>>>>> 3f723775cc55555e43504763b467e804a6956082

    # Fix the URI for Fly configuration
    database_uri = os.getenv("DATABASE_URL")
    database_uri = database_uri.replace("postgres://", "postgresql://")
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

    db.init_app(app)

    return app
