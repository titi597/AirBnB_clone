#!/usr/bin/python3
"""testing basemodel."""
import unittest
import os
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    def test_instance_attributes(self):
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_save_method(self):
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_to_dict_method(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('id', obj_dict)
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertIn('created_at', obj_dict)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_str_method(self):
        obj = BaseModel()
        obj_str = str(obj)
        expected_str = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(obj_str, expected_str)

    def test_init_with_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertEqual(obj.id, new_obj.id)
        self.assertEqual(obj.created_at, new_obj.created_at)
        self.assertEqual(obj.updated_at, new_obj.updated_at)


if __name__ == '__main__':
    unittest.maiin()
