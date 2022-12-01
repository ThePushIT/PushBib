from repositories.reference_repository import reference_repository as default_reference_repository
#from models.books import Book


class ReferenceService:
    def __init__(self, reference_repository=default_reference_repository):
        self._reference_repository = reference_repository

    def create_book_reference(self, user_id, authors, title, year, publisher):
        # muutetaan mahdollisesti myöhemmin toimimaan Book Modelin avulla
        # syötteen oikeellisuuden tarkistaminen
        self._reference_repository.insert_book_reference(
            user_id, authors, title, year, publisher)

    def get_references(self, user_id):
        return self._reference_repository.fetch_all_references(user_id)


reference_service = ReferenceService()
