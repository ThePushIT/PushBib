import unittest
from repositories.reference_repository import reference_repository

class TestReferenceRepository(unittest.TestCase):
    def setUp(self):
        reference_repository.delete_all()

    def test_create(self):
        reference_repository.create(1, 'jee', 'jee', 2000)
        #references = reference_repository.find_all()
        # self.assertEqual(references, 1)