import unittest
from services.user_service import user_service
from flask import session
from init_db import initialize_db
from app import create_app

app = create_app()

request_ctx = app.test_request_context()
request_ctx.push()

class TestUserService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #Alustaa tietokannan ennen testejä.
        initialize_db()

    def setUp(self):
        #Poistaa kaikki käyttäjät ennen jokaista testiä.
        user_service.delete_all_users()
    
    def test_can_register(self):
        self.assertTrue(user_service.register("user", "pass"))
    
    def test_cannot_register_with_taken_username(self):
        user_service.register("user", "pass")
        self.assertFalse(user_service.register("user", "pass2"))
    
    def test_can_login_after_register(self):
        user_service.register("user", "pass")
        self.assertTrue(user_service.login("user", "pass"))
    
    def test_cannot_login_with_incorrect_password(self):
        user_service.register("user", "pass")
        self.assertFalse(user_service.login("user", "wrong"))
    
    def test_cannot_login_with_nonexistent_username(self):
        self.assertFalse(user_service.login("user", "pass"))
        self.assertEqual(user_service.get_id(), 0)
    
