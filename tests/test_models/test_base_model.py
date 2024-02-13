#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict_returns_dict(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_class_name(self):
        obj_dict = self.base_model.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_to_dict_contains_created_at(self):
        obj_dict = self.base_model.to_dict()
        self.assertIn('created_at', obj_dict)

    def test_to_dict_contains_updated_at(self):
        obj_dict = self.base_model.to_dict()
        self.assertIn('updated_at', obj_dict)

    def test_to_dict_created_at_iso_format(self):
        obj_dict = self.base_model.to_dict()
        created_at_iso_format = datetime.fromisoformat(obj_dict['created_at'])
        self.assertEqual(self.base_model.created_at, created_at_iso_format)

    def test_to_dict_updated_at_iso_format(self):
        obj_dict = self.base_model.to_dict()
        updated_at_iso_format = datetime.fromisoformat(obj_dict['updated_at'])
        self.assertEqual(self.base_model.updated_at, updated_at_iso_format)


if __name__ == '__main__':
    unittest.main()
