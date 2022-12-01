from repositories.user_repository import user_repository as default_user_repository


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def register(self, username, password):
        if self._user_repository.create(username, password):
            return self.login(username, password)

        return False

    def login(self, username, password):
        if self._user_repository.validate(username, password):
            return True

    def get_id(self):
        return self._user_repository.id()


user_service = UserService()
