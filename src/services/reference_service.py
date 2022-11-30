from repositories.reference_repository import reference_repository as default_reference_repository
#from models.books import Book

class ReferenceService:
    def __init__(self, reference_repository=default_reference_repository):
        self._reference_repository = reference_repository

    def create_reference(self, user_id, name, authors, year):
        # muutetaan mahdollisesti myöhemmin toimimaan Book Modelin avulla

        #TODO
        # syötteen oikeellisuuden tarkistaminen
        self._reference_repository.create(user_id, name, authors, year)

reference_service = ReferenceService()