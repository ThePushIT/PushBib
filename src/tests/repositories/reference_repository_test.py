import unittest
from repositories.reference_repository import reference_repository
from repositories.user_repository import user_repository
from services.user_service import user_service
from services.reference_service import reference_service
from unittest.mock import patch
from app import app


class TestReferenceRepository(unittest.TestCase):
    def setUp(self):
        reference_repository.delete_all_books()

    def test_insert_book_reference_succeeds(self):
        # ongelmat tällä hetkellä
        # testi tarvis session mut testitapaukset ei hyväksy html viestintää
        # tän takia rekisteröinti ei onnistu
        # jos rekisteröinti ei onnistu niin kirjan lisääminen ei onnistu
        #user_service.register('olivia', 'jeejeejee')
        self.assertTrue(
            reference_repository.insert_book_reference(
                1, "Anonyymi", "Kiva kirja", 2020, "Otava")
        )
