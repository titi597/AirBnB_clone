#!/usr/bin/python3
"""testing file storage."""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Initialize FileStorage and remove the existing JSON file
        self.storage = FileStorage()
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def tearDown(self):
        # Clean up by removing the JSON file
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_save_and_reload_base_model(self):
        # Create a BaseModel instance and save it
        obj = BaseModel()
        obj.save()

        # Reload the storage and check if the object is in the storage
        self.storage.reload()
        self.assertIn(f"BaseModel.{obj.id}", self.storage.all())

    def test_save_and_reload_user(self):
        # Create a User instance and save it
        obj = User()
        obj.save()

        # Reload the storage and check if the object is in the storage
        self.storage.reload()
        self.assertIn(f"User.{obj.id}", self.storage.all())

    def test_save_and_reload_state(self):
        # Create a State instance and save it
        obj = State()
        obj.save()

        # Reload the storage and check if the object is in the storage
        self.storage.reload()
        self.assertIn(f"State.{obj.id}", self.storage.all())

    def test_save_and_reload_city(self):
        # Create a City instance and save it
        obj = City()
        obj.save()

        # Reload the storage and check if the object is in the storage
        self.storage.reload()
        self.assertIn(f"City.{obj.id}", self.storage.all())

    def test_save_and_reload_amenity(self):
        # Create an Amenity instance and save it
        obj = Amenity()
        obj.save()

        # Reload the storage and check if the object is in the storage
        self.storage.reload()
        self.assertIn(f"Amenity.{obj.id}", self.storage.all())

    def test_save_and_reload_place(self):
        # Create a Place instance and save it
        obj = Place()
        obj.save()

        # Reload the storage and check if the object is in the storage
        self.storage.reload()
        self.assertIn(f"Place.{obj.id}", self.storage.all())

    def test_save_and_reload_review(self):
        # Create a Review instance and save it
        obj = Review()
        obj.save()

        # Reload the storage and check if the object is in the storage
        self.storage.reload()
        self.assertIn(f"Review.{obj.id}", self.storage.all())


if __name__ == '__main__':
    unittest.main()
