from sqlalchemy.exc import ProgrammingError
from database import db
from app import create_app

app = create_app()
app.app_context().push()


def drop_tables():
    db.session.execute("""
        DROP TABLE IF EXISTS users, books, articles, inproceedings CASCADE;
    """)


def create_table(sql_string: str, table_name: str):
    try:
        db.session.execute(sql_string)
        db.session.commit()
        print(f"Table {table_name} created")
    except ProgrammingError:
        print(f"Table {table_name} already exists, passing.")


def create_user_table():
    sql = """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        );
        """

    create_table(sql, "users")


def create_books():
    sql = """
        CREATE TABLE books (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users,
            authors TEXT,
            title TEXT,
            year TEXT,
            publisher TEXT
        );
        """
    create_table(sql, "books")


def create_articles():
    sql = """
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
        """
    create_table(sql, "articles")


def create_inproceedings():
    sql = """
    CREATE TABLE inproceedings (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users,
            authors TEXT,
            title TEXT,
            year TEXT,
            booktitle TEXT
        );
        """
    create_table(sql, "inproceedings")


def create_reference_tables():
    create_books()
    create_articles()
    create_inproceedings()


def initialize_db():
    drop_tables()
    create_user_table()
    create_reference_tables()


if __name__ == "__main__":
    initialize_db()
