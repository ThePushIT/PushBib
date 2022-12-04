from repositories.reference_repository import reference_repository as default_reference_repository


class ReferenceService:
    def __init__(self, reference_repository=default_reference_repository):
        self._reference_repository = reference_repository

    # syötteiden oikeellisuuden tarkistaminen
    def create_book_reference(self, user_id, authors, title, year, publisher):
        self._reference_repository.insert_book_reference(
            user_id, authors, title, year, publisher)

    def create_article_reference(self, user_id, authors, title, journal, year, volume, pages):
        self._reference_repository.insert_article_reference(
            user_id, authors, title, journal, year, volume, pages)

    def create_inproceeding_reference(self, user_id, authors, title, year, booktitle):
        self._reference_repository.insert_inproceeding_reference(
            user_id, authors, title, year, booktitle)

    def get_book_references(self, user_id):
        return self._reference_repository.fetch_book_references(user_id)

    def get_article_references(self, user_id):
        return self._reference_repository.fetch_article_references(user_id)

    def get_inproceeding_references(self, user_id):
        return self._reference_repository.fetch_inproceeding_references(user_id)

    def delete_all_book_references(self):
        return self._reference_repository.delete_all_books()


reference_service = ReferenceService()
