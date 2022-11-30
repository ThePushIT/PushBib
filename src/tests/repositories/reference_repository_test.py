import unittest
from repositories.reference_repository import reference_repository


class TestReferenceRepository(unittest.TestCase):
    def setUp(self):
        reference_repository.delete_all_books()

    def test_insert_book_reference_succeeds(self):
        self.assertTrue(
            reference_repository.insert_book_reference(1,"Anonyymi", "Kiva kirja", 2020, "Otava")
            )
