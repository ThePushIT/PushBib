from database import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

class UserRepository:
    def create(self, username, password):
        hash_value = generate_password_hash(password)
        try:
            sql = "INSERT INTO USERS (username, password) VALUES (:username, :password)"
            db.session.execute(sql, {"username":username, "password":hash_value})
            db.session.commit()
        except:
            return False

        return True

user_repository = UserRepository()