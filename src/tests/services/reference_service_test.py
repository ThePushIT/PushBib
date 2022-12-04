import unittest
from services.reference_service import reference_service
from repositories.user_repository import user_repository
from services.reference_service import reference_service
from app import create_app

app = create_app()

request_ctx = app.test_request_context()
request_ctx.push()

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
        reference_service.delete_all_book_references()

    def test_insert_book_reference_succeeds(self):
        reference_service.create_book_reference(
            '1', "Anonyymi", "Kiva kirja", 2020, "Otava")
        books = reference_service.get_references(1)
        print(books)
        self.assertEqual(1, len(books))
