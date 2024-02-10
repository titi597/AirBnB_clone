#!/usr/bin/python3
"""testing file storage."""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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

    def test_save_and_reload(self):
        # Create a BaseModel instance and save it
        obj = BaseModel()
        obj.save()

        # Reload the storage and check if the object is in the storage
        self.storage.reload()
        self.assertIn(f"BaseModel.{obj.id}", self.storage.all())

    def test_new_method(self):
        # Create a BaseModel instance and add it to the storage
        obj = BaseModel()
        self.storage.new(obj)

        # Check if the object is in the storage
        self.assertIn(f"BaseModel.{obj.id}", self.storage.all())

    def test_save_method(self):
        # Create a BaseModel instance and add it to the storage
        obj = BaseModel()
        self.storage.new(obj)

        # Save the storage and check if the JSON file is created
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload_method_without_file(self):
        # Ensure reload doesn't raise an exception when the file doesn't exist
        self.storage.reload()

    def test_reload_method_with_file(self):
        # Create a BaseModel instance and save it
        obj = BaseModel()
        obj.save()

        # Reload the storage and check if the object is in the storage
        self.storage.reload()
        self.assertIn(f"BaseModel.{obj.id}", self.storage.all())


if __name__ == '__main__':
    unittest.main()
