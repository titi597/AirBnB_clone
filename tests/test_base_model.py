#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.__init__ import storage

class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_save_method(self):
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save(storage)
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_to_dict_method(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_init_with_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertIsInstance(new_obj, BaseModel)
        self.assertEqual(new_obj.id, obj.id)
        self.assertEqual(new_obj.created_at, obj.created_at)
        self.assertEqual(new_obj.updated_at, obj.updated_at)

if __name__ == '__main__':
    unittest.main()
