from flask import session

class LanguageRepository:
    def set_language(self, lang):
        session["lang"] = lang

language_repository = LanguageRepository()
