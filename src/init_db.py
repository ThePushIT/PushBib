from sqlalchemy.exc import ProgrammingError
from database import db
from app import create_app

app = create_app()
app.app_context().push()

SQL_TABLES = {
    "user": """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        );
        """,
    "books": """
        CREATE TABLE books (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users,
            authors TEXT,
            title TEXT,
            year TEXT,
            publisher TEXT
        );
        """,
    "articles": """
        CREATE TABLE articles (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users,
            authors TEXT,
            title TEXT,
            journal TEXT,
            year TEXT,
            volume INT,
            pages TEXT
        );
        """,
    "inproceedings": """
        CREATE TABLE inproceedings (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users,
            authors TEXT,
            title TEXT,
            year TEXT,
            booktitle TEXT
        );
        """,
}


def drop_tables():
    db.session.execute(
        """
        DROP TABLE IF EXISTS users, books, articles, inproceedings CASCADE;
    """
    )


def create_tables(tables: dict):
    for table_name, sql_str in tables.items():
        try:
            db.session.execute(sql_str)
            db.session.commit()
            print(f"Table {table_name} created")
        except ProgrammingError:
            print(f"Table {table_name} already exists, passing.")


def initialize_db():
    drop_tables()
    create_tables(SQL_TABLES)


if __name__ == "__main__":
    initialize_db()
