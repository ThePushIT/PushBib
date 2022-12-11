import unittest
import filecmp
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
        user_repository.create("testuser", "testpassword")

    def setUp(self):
        # ajetaan ennen jokaista testiä
        reference_service.delete_all_references()

    def test_insert_book_reference_succeeds(self):
        reference_service.create_book_reference(
            "1", "Vallaton, Ville", "Jäätelöhistoriikki", 2020, "Otava")
        books = reference_service.get_book_references(1)
        self.assertEqual(1, len(books))

    def test_insert_article_reference_succeeds(self):
        reference_service.create_article_reference(
            "1", "Collins, Allan et al", "Cognitive Apprenticeship", "American Educator", 1991, 6, "38-46")
        articles = reference_service.get_article_references(1)
        self.assertEqual(1, len(articles))

    def test_insert_inproceeding_reference_succeeds(self):
        reference_service.create_inproceeding_reference(
            "1", "Luukkainen et al", "Extreme Apprenticeship Method", 2011, "SIGCSE '11: \
            Proceedings of the 42nd SIGCSE technical symposium on Computer science education")
        inproceedings = reference_service.get_inproceeding_references(1)
        self.assertEqual(1, len(inproceedings))

    def test_insert_misc_reference_succeeds(self):
        reference_service.create_misc_reference(
            "1", "NASA", "Pluto: The 'Other' Red Planet", "https://www.nasa.gov/nh/pluto-the-other-red-planet", 2015, "Accessed: 2018-12-06")
        misc = reference_service.get_misc_references(1)
        self.assertEqual(1, len(misc))

    def test_get_all_references_by_id_returns_all_users_references(self):
        reference_service.create_book_reference(
            "1", "Vallaton, Ville", "Jäätelöhistoriikki", 2020, "Otava")
        reference_service.create_article_reference(
            "1", "Collins, Allan et al", "Cognitive Apprenticeship", "American Educator", 1991, 6, "38-46")
        reference_service.create_inproceeding_reference(
            "1", "Luukkainen et al", "Extreme Apprenticeship Method", 2011, "SIGCSE '11: \
            Proceedings of the 42nd SIGCSE technical symposium on Computer science education")
        reference_service.create_misc_reference(
            "1", "NASA", "Pluto: The 'Other' Red Planet", "https://www.nasa.gov/nh/pluto-the-other-red-planet", 2015, "Accessed: 2018-12-06")

        references = reference_service.get_all_references_by_user_id(1)
        self.assertEqual(len(references), 4)

    def test_convert_books_into_dictionaries_returns_correct_dictionary(self):
        reference_service.create_book_reference(
            "1", "Vallaton, Ville", "Jäätelöhistoriikki", 2020, "Otava")
        books = reference_service.get_book_references(1)
        book_dict = reference_service.convert_books_into_dictionaries(books)[0]

        correct = {
            "Author(s)": "Vallaton, Ville",
            "Title": "Jäätelöhistoriikki",
            "Year": "2020",
            "Publisher": "Otava"
        }

        self.assertEqual(book_dict, correct)

    def test_convert_articles_into_dictionaries_returns_correct_dictionary(self):
        reference_service.create_article_reference(
            "1", "Collins, Allan et al", "Cognitive Apprenticeship", "American Educator", 1991, 6, "38-46")
        articles = reference_service.get_article_references(1)
        article_dict = reference_service.convert_articles_into_dictionaries(articles)[0]

        correct = {
            "Author(s)": "Collins, Allan et al",
            "Title": "Cognitive Apprenticeship",
            "Journal": "American Educator",
            "Year": "1991",
            "Volume": 6,
            "Pages": "38-46"
        }

        self.assertEqual(article_dict, correct)

    def test_convert_inproceedings_into_dictionaries_returns_correct_dictionary(self):
        reference_service.create_inproceeding_reference(
            "1", "Luukkainen et al", "Extreme Apprenticeship Method", 2011, "SIGCSE '11: \
            Proceedings of the 42nd SIGCSE technical symposium on Computer science education")
        inproceedings = reference_service.get_inproceeding_references(1)
        inproceeding_dict = reference_service.convert_inproceedings_into_dictionaries(inproceedings)[0]

        correct = {
            "Author(s)": "Luukkainen et al",
            "Title": "Extreme Apprenticeship Method",
            "Year": "2011",
            "Booktitle": "SIGCSE '11: \
            Proceedings of the 42nd SIGCSE technical symposium on Computer science education"
        }

        self.assertEqual(inproceeding_dict, correct)

    def test_convert_misc_into_dictionaries_returns_correct_dictionary(self):
        reference_service.create_misc_reference(
            "1", "NASA", "Pluto: The 'Other' Red Planet", "https://www.nasa.gov/nh/pluto-the-other-red-planet", 2015, "Accessed: 2018-12-06")
        misc = reference_service.get_misc_references(1)
        misc_dict = reference_service.convert_misc_into_dictionaries(misc)[0]

        correct = {
            "Author(s)": "NASA",
            "Title": "Pluto: The 'Other' Red Planet",
            "Howpublished": "https://www.nasa.gov/nh/pluto-the-other-red-planet",
            "Year": "2015",
            "Note": "Accessed: 2018-12-06"
        }

        self.assertEqual(misc_dict, correct)

    def test_sort_references_alphabetically_by_author_returns_correct_order(self):
        reference_service.create_book_reference(
            "1", "Vallaton, Ville", "Jäätelöhistoriikki", 2020, "Otava")
        reference_service.create_article_reference(
            "1", "Collins, Allan et al", "Cognitive Apprenticeship", "American Educator", 1991, 6, "38-46")
        reference_service.create_inproceeding_reference(
            "1", "Luukkainen et al", "Extreme Apprenticeship Method", 2011, "SIGCSE '11: \
            Proceedings of the 42nd SIGCSE technical symposium on Computer science education")
        reference_service.create_misc_reference(
            "1", "NASA", "Pluto: The 'Other' Red Planet", "https://www.nasa.gov/nh/pluto-the-other-red-planet", 2015, "Accessed: 2018-12-06")

        references = reference_service.get_all_references_by_user_id(1)
        references = reference_service.sort_references_alphabetically_by_author(references)

        self.assertEqual(references[0]["Author(s)"], "Collins, Allan et al")
        self.assertEqual(references[1]["Author(s)"], "Luukkainen et al")
        self.assertEqual(references[2]["Author(s)"], "NASA")
        self.assertEqual(references[3]["Author(s)"], "Vallaton, Ville")

    def test_cannot_access_other_users_data(self):
        user_id = 1
        reference_service.create_article_reference(user_id, "J. Jonah Jameson", "An article", "The Times", 2022, 1, "1-24")
        reference_service.create_book_reference(user_id, "Jesus Christ", "The Holy Bible", 1, "The Vatican")
        reference_service.create_inproceeding_reference(user_id, "Me", "What is an inproceeding?", 2020, "I can't come up with a fun title :/")
        reference_service.create_misc_reference(user_id, "Miscella", "Miscellaneous Title: The Electric Boogaloo", "https://url.url", 1991, "Noteworthy")

        user_repository.create("user2", "password2")
        user_id = 2
        self.assertEqual(len(reference_service.get_article_references(user_id)), 0)
        self.assertEqual(len(reference_service.get_book_references(user_id)), 0)
        self.assertEqual(len(reference_service.get_inproceeding_references(user_id)), 0)
        self.assertEqual(len(reference_service.get_misc_references(user_id)), 0)
    
    def test_bibtex_outputs_correctly(self):
        user_id = 1
        reference_service.create_article_reference(user_id, "J. Jonah Jameson", "An article", "The Times", 2022, 1, "1-24")
        reference_service.create_book_reference(user_id, "Jesus Christ", "The Holy Bible", 1, "The Vatican")
        reference_service.create_inproceeding_reference(user_id, "Me", "What is an inproceeding?", 2020, "I can't come up with a fun title :/")
        reference_service.create_misc_reference(user_id, "Miscella", "Miscellaneous Title: The Electric Boogaloo", "https://url.url", 1991, "Noteworthy")

        file_path = reference_service.create_bibtex_file(user_id)

        reference_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_bib_output_should_be.bib")

        self.assertTrue(filecmp.cmp(file_path, reference_file))
