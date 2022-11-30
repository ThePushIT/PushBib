from sqlalchemy.exc import ProgrammingError
from database import db
from app import create_app

app = create_app()
app.app_context().push()

def drop_tables():
    db.session.execute("""
        DROP TABLE IF EXISTS users CASCADE;
    """)

    db.session.execute("""
        DROP TABLE IF EXISTS books CASCADE;
    """)



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
        print('table users created')
    except ProgrammingError:
        print("Table users already exists, passing.")

    try:
        db.session.execute("""
        CREATE TABLE books (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users,
            name TEXT,
            authors TEXT,
            year INT
        );
        """)
        db.session.commit()
        print('table books created')
    except ProgrammingError:
        print("Table books already exists, passing.")

def initialize_db():
    drop_tables()
    create_tables()

if __name__ == "__main__":
    initialize_db()
