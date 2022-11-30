from database import db

class ReferenceRepository:
    def __init__(self):
        pass

    def insert_book_reference(self, user_id, authors, title, year, publisher):
        # muutetaan mahdollisesti myöhemmin toimimaan Book Modelin avulla
        # tällöin saa parametrina Bookin
        try:
            print('ollaan tryssa')
            sql = """INSERT INTO books (user_id, authors, title, year, publisher) 
                    VALUES (:user_id, :authors, :title, :year, :publisher)"""
            db.session.execute(sql, 
                                {
                                "user_id":user_id,
                                "authors":authors,
                                "title":title,
                                "year":year,
                                "publisher":publisher
                                }
                                )
            db.session.commit()
        except:
            return False
        return True

    def fetch_all_references(self, user_id):
        # change to accommodate all types of references, not just books
        try:
            print('ollaan tryssa')
            sql = """SELECT authors, title, year, publisher
                     FROM books
                     WHERE user_id=:user_id
                     ORDER BY authors"""
            return db.session.execute(sql, {"user_id": user_id}).fetchall()
        except:
            return False

    def delete_all_books(self):
        try:
            db.session.execute("""DELETE FROM books""")
            db.session.commit()
            return True
        except:
            return False


reference_repository = ReferenceRepository()
