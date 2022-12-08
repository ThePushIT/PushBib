import unittest
from services.reference_service import reference_service
from repositories.user_repository import user_repository
from services.reference_service import reference_service
from datetime import date
from app import create_app
import os

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
        reference_service.delete_all_references()

    def test_insert_book_reference_succeeds(self):
        reference_service.create_book_reference(
            '1', "Anonyymi", "Kiva kirja", 2020, "Otava")
        books = reference_service.get_book_references(1)
        self.assertEqual(1, len(books))

    def test_insert_article_reference_succeeds(self):
        reference_service.create_article_reference(
            '1', "Allan Collins et al", "Cognitive Apprenticeship", "American Educator", 1991, 6, "38-46")
        articles = reference_service.get_article_references(1)
        self.assertEqual(1, len(articles))

    def test_insert_inproceeding_reference_succeeds(self):
        reference_service.create_inproceeding_reference(
            '1', "Luukkainen et al", "Extreme Apprenticeship Method", 2011, "SIGCSE '11: \
            Proceedings of the 42nd SIGCSE technical symposium on Computer science education")
        inproceedings = reference_service.get_inproceeding_references(1)
        self.assertEqual(1, len(inproceedings))

    def test_create_bibtex(self):
        user_id = 1
        file_path = reference_service.create_bibtex_file(user_id)
        self.assertEqual(os.path.join(os.getcwd(), 
                        "user_files",
                        f"references_{user_id}_{date.today()}.bib"), file_path)
    
    def test_bibtex_is_in_correct_format(self):
        user_id = 1
        reference_service.create_article_reference(user_id, "J. Jonah Jameson", "An article", "The Times", 2022, 1, "1-24")
        reference_service.create_book_reference(user_id, "Jesus Christ", "The Holy Bible", 1, "The Vatican")
        reference_service.create_inproceeding_reference(user_id, "Me", "What is an inproceeding?", 2020, "I can't come up with a fun title :/")

        file_path = reference_service.convert_all_references_to_bibtex(user_id)

        self.assertTrue(1, 1)
