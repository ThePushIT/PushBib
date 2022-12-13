import unittest
from services.language_service import language_service
from app import create_app
from index import get_locale


app = create_app()

request_ctx = app.test_request_context()
request_ctx.push()

class TestLanguageService(unittest.TestCase):
    def test_change_language_works(self):
        language_service.set_language("fi")
        self.assertEqual(get_locale(), "fi")
        language_service.set_language("en")
        self.assertEqual(get_locale(), "en")