from sqlalchemy.exc import ProgrammingError
from database import db
from app import create_app

app = create_app()
app.app_context().push()

def create_tables():
    try:
        db.session.execute("""
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        );
        """)
        db.session.commit()
    except ProgrammingError:
        print("Table already exists, passing.")

if __name__ == "__main__":
    create_tables()
