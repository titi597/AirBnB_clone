#!/usr/bin/python3
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_attributes(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_unique(self):
        other_model = BaseModel()
        self.assertNotEqual(self.base_model.id, other_model.id)

    def test_str_method(self):
        expected_str = "[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_create_instance_from_dict(self):
        obj_dict = self.base_model.to_dict()
        new_model = BaseModel(**obj_dict)
        self.assertEqual(new_model.id, self.base_model.id)
        self.assertEqual(new_model.created_at, self.base_model.created_at)
        self.assertEqual(new_model.updated_at, self.base_model.updated_at)


if __name__ == '__main__':
    unittest.main()
