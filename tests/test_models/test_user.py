#!/usr/bin/python3
"""Unittest for User class"""
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def test_instance(self):
        """Test creating an instance of User"""
        user = User()
        self.assertIsInstance(user, User)

    def test_attributes(self):
        """Test attributes of User"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_inheritance(self):
        """Test inheritance"""
        user = User()
        self.assertTrue(issubclass(type(user), User))

    def test_created_at(self):
        """Test created_at attribute"""
        user = User()
        self.assertIsInstance(user.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at attribute"""
        user = User()
        self.assertIsInstance(user.updated_at, datetime)

    def test_str_representation(self):
        """Test __str__ method"""
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), string)

    def test_to_dict(self):
        """Test to_dict method"""
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["created_at"], user.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"], user.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
