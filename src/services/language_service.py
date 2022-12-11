from repositories.language_repository import language_repository as default_language_repository

class LanguageService:
    def __init__(self, language_repository = default_language_repository) -> None:
        self.language_repository = language_repository

    def set_language(self, lang):
        self.language_repository.set_language(lang)

language_service = LanguageService()
