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
        DROP TABLE IF EXISTS references_table CASCADE;
    """)
    db.session.commit()



def create_tables():
    try:
        db.session.execute("""
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username TEXT,
            password TEXT
        );
        """)
        db.session.commit()
        print('table users created')
    except ProgrammingError:
        print("Table users already exists, passing.")

    try:
        db.session.execute("""
        CREATE TABLE references_table (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users,
            name TEXT,
            authors TEXT,
            type TEXT,
            year INT
        );
        """)
        db.session.commit()
        print('table references created')
    except ProgrammingError:
        print("Table references already exists, passing.")

def initialize_db():
    drop_tables()
    create_tables()

if __name__ == "__main__":
    initialize_db()
