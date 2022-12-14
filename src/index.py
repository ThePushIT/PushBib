from flask_babel import Babel
from flask import session, request
from app import create_app
from config import LANGUAGES

print('ollaan indexissa')

app = create_app()
babel = Babel()
babel.init_app(app)

@babel.localeselector
def get_locale():
    try:
        return session["lang"]
    except KeyError:
        session["lang"] = request.accept_languages.best_match(LANGUAGES.keys())
        return session["lang"]

if __name__ == "__main__":
    app.run()
