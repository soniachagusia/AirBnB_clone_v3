import unittest
from models import storage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.storage = storage
        self.storage.reload()

    def test_get(self):
        """Test the get method"""
        obj = BaseModel()
        obj_id = obj.id
        self.storage.new(obj)
        self.storage.save()
        self.assertIs(self.storage.get(BaseModel, obj_id), obj)
        self.assertIsNone(self.storage.get(BaseModel, "nonexistent_id"))

    def test_count(self):
        """Test the count method"""
        initial_count = self.storage.count()
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertEqual(self.storage.count(), initial_count + 1)
        self.assertEqual(self.storage.count(BaseModel), initial_count + 1)

if __name__ == '__main__':
    unittest.main()
