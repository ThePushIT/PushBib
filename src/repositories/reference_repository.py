from database import db

class ReferenceRepository:
    def __init__(self):
        pass

    def create(self, user_id, name, authors, year):
        # muutetaan mahdollisesti myöhemmin toimimaan Book Modelin avulla
        # tällöin saa parametrina Bookin
        try:
            sql = """INSERT INTO books (user_id, name, authors, year) 
                    VALUES (:user_id, :name, :authors, :year)"""
            db.session.execute(sql, 
                                {
                                "user_id":user_id,
                                "name":name,
                                "authors":authors,
                                "year":year
                                }
                                )
            db.session.commit()
        except:
            return False

        return True

    def delete_all(self):
        try:
            sql = """DELETE ALL FROM books"""
            db.session.execute(sql)
            db.session.commit()
        except:
            return False

        return True


reference_repository = ReferenceRepository()