from sqlalchemy.exc import ProgrammingError
from database import db
from app import create_app

app = create_app()
app.app_context().push()


def drop_tables():
    db.session.execute("""
        DROP TABLE IF EXISTS users, books, articles, inproceedings CASCADE;
    """)

def create_user_table():
    try:
        db.session.execute("""
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        );
        """)
        db.session.commit()
        print('Table users created')
    except ProgrammingError:
        print("Table users already exists, passing.")

def create_reference_tables():
    try:
        db.session.execute("""
        CREATE TABLE books (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users,
            authors TEXT,
            title TEXT,
            year INT,
            publisher TEXT
        );
        """)
        db.session.commit()
        print('Table books created')
    except ProgrammingError:
        print("Table books already exists, passing.")

    try:
        db.session.execute("""
        CREATE TABLE articles (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users,
            authors TEXT,
            title TEXT,
            journal TEXT,
            year INT,
            volume INT,
            pages TEXT
        );
        """)
        db.session.commit()
        print('Table articles created')
    except ProgrammingError:
        print("Table articles already exists, passing.")

    try:
        db.session.execute("""
        CREATE TABLE inproceedings (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users,
            authors TEXT,
            title TEXT,
            year INT,
            booktitle TEXT
        );
        """)
        db.session.commit()
        print('Table inproceedings created')
    except ProgrammingError:
        print("Table inproceedings already exists, passing.")


def initialize_db():
    drop_tables()
    create_user_table()
    create_reference_tables()


if __name__ == "__main__":
    initialize_db()
