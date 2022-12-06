# import secrets
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.exc import ProgrammingError, IntegrityError
from database import db


class UserRepository:
    def create(self, username, password):
        hash_value = generate_password_hash(password)
        try:
            sql = "INSERT INTO USERS (username, password) VALUES (:username, :password)"
            db.session.execute(
                sql, {"username": username, "password": hash_value})
            db.session.commit()
        except IntegrityError:
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

    def end_session(self):
        del session["user_id"]

    def id(self):
        return session.get("user_id", 0)

    def delete_all_users(self):
        session.clear()
        sql = 'DELETE FROM users'
        try:
            db.session.execute(sql)
            db.session.commit()
            return True
        except ProgrammingError:
            return False


user_repository = UserRepository()
