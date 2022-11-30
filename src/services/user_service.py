from repositories.user_repository import user_repository as default_user_repository

class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def register(self, username, password, password_again):
        if password != password_again:
            return (False, "Salasanat eroavat")
        elif len(username) < 5:
            return (False, "Tunnuksen tulee olla vähintään 5 merkkiä pitkä")
        elif len(password) < 8:
            return (False, "Salasanan tulee olla vähintään 8 merkkiä pitkä")
        elif len(password) > 25 or len(username) > 25:
            return (False, "Käyttäjätunnus ja/tai salasana on liian pitkä")

        if self._user_repository.create(username, password):
            return (True, "")
            #self.login(username, password)
        else:
            return (False, "Valitse toinen käyttäjätunnus")


user_service = UserService()