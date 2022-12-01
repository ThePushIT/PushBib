# import secrets
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from database import db
from sqlalchemy.exc import ProgrammingError


class UserRepository:
    def create(self, username, password):
        hash_value = generate_password_hash(password)
        try:
            sql = "INSERT INTO USERS (username, password) VALUES (:username, :password)"
            db.session.execute(
                sql, {"username": username, "password": hash_value})
            db.session.commit()
        except ProgrammingError:
            return False

        return True

    def validate(self, username, password):
        print("validateen saavuttu")
        sql = "SELECT id, password FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username": username})
        user = result.fetchone()
        if not user:
            return False

        if check_password_hash(user.password, password):
            self.create_session(user.id)
            return True

        return False

    def create_session(self, user_id):
        session["user_id"] = user_id

    def id(self):
        return session.get("user_id", 0)


user_repository = UserRepository()
