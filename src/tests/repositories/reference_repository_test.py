import unittest
from repositories.reference_repository import reference_repository
from repositories.user_repository import user_repository
from services.user_service import user_service
from services.reference_service import reference_service


class TestReferenceRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # ajetaan ennen kaikkia testitapauksia
        # tyhjennetään testitietokanta käyttäjistä jotta id:t oikein
        # luodaan testikäyttäjä jolle voidaan lisätä kirjoja
        user_repository.delete_all_users()
        user_repository.create('testuser', 'testpassword')

    def setUp(self):
        # ajetaan ennen jokaista testiä
        reference_repository.delete_all_books()

    def test_insert_book_reference_succeeds(self):
        reference_repository.insert_book_reference(
                            '1', "Anonyymi", "Kiva kirja", 2020, "Otava")
        books = reference_repository.fetch_all_references(1)
        print(books)
        self.assertEqual(1, len(books))

