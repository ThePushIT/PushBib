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


reference_repository = ReferenceRepository()