from sqlalchemy.exc import ProgrammingError
from database import db


class ReferenceRepository:
    def __init__(self):
        pass

    def insert_book_reference(self, user_id, authors, title, year, publisher):
        try:
            sql = """INSERT INTO books (user_id, authors, title, year, publisher)
                    VALUES (:user_id, :authors, :title, :year, :publisher)"""
            db.session.execute(sql,
                               {
                                   "user_id": user_id,
                                   "authors": authors,
                                   "title": title,
                                   "year": year,
                                   "publisher": publisher
                               }
                               )
            db.session.commit()
        except ProgrammingError:
            return False
        return True

    def insert_article_reference(self, user_id, authors, title, journal, year, volume, pages):
        try:
            sql = """INSERT INTO articles (user_id, authors, title, journal, year, volume, pages)
                    VALUES (:user_id, :authors, :title, :journal, :year, :volume, :pages)"""
            db.session.execute(sql,
                               {
                                   "user_id": user_id,
                                   "authors": authors,
                                   "title": title,
                                   "journal": journal,
                                   "year": year,
                                   "volume": volume,
                                   "pages": pages
                               }
                               )
            db.session.commit()
        except ProgrammingError:
            return False
        return True

    def insert_inproceeding_reference(self, user_id, authors, title, year, booktitle):
        try:
            sql = """INSERT INTO inproceedings (user_id, authors, title, year, booktitle)
                    VALUES (:user_id, :authors, :title, :year, :booktitle)"""
            db.session.execute(sql,
                               {
                                   "user_id": user_id,
                                   "authors": authors,
                                   "title": title,
                                   "year": year,
                                   "booktitle": booktitle
                               }
                               )
            db.session.commit()
        except ProgrammingError:
            return False
        return True

    def insert_misc_reference(self, user_id, authors, title, howpublished, year, note):
        try:
            sql = """INSERT INTO misc (user_id, authors, title, howpublished, year, note)
                    VALUES (:user_id, :authors, :title, :howpublished, :year, :note)"""
            db.session.execute(sql,
                               {
                                   "user_id": user_id,
                                   "authors": authors,
                                   "title": title,
                                   "howpublished": howpublished,
                                   "year": year,
                                   "note": note
                               }
                               )
            db.session.commit()
        except ProgrammingError:
            return False
        return True

    def fetch_book_references(self, user_id):
        try:
            sql = """SELECT authors, title, year, publisher
                     FROM books
                     WHERE user_id=:user_id
                     ORDER BY authors"""
            return db.session.execute(sql, {"user_id": user_id}).fetchall()
        except ProgrammingError:
            return False

    def fetch_article_references(self, user_id):
        try:
            sql = """SELECT authors, title, journal, year, volume, pages
                     FROM articles
                     WHERE user_id=:user_id
                     ORDER BY authors"""
            return db.session.execute(sql, {"user_id": user_id}).fetchall()
        except ProgrammingError:
            return False

    def fetch_inproceeding_references(self, user_id):
        try:
            sql = """SELECT authors, title, year, booktitle
                     FROM inproceedings
                     WHERE user_id=:user_id
                     ORDER BY authors"""
            return db.session.execute(sql, {"user_id": user_id}).fetchall()
        except ProgrammingError:
            return False

    def fetch_misc_references(self, user_id):
        try:
            sql = """SELECT authors, title, howpublished, year, note
                     FROM misc
                     WHERE user_id=:user_id
                     ORDER BY authors"""
            return db.session.execute(sql, {"user_id": user_id}).fetchall()
        except ProgrammingError:
            return False

    def delete_all_references(self):
        try:
            db.session.execute("DELETE FROM books")
            db.session.execute("DELETE FROM articles")
            db.session.execute("DELETE FROM inproceedings")
            db.session.execute("DELETE FROM misc")
            db.session.commit()
            return True
        except ProgrammingError:
            return False


reference_repository = ReferenceRepository()
