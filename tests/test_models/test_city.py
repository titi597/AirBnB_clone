#!/usr/bin/python3
"""Unit test for City class"""
import unittest
import os
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def setUp(self):
        """Setup method"""
        self.city = City()

    def tearDown(self):
        """Teardown method"""
        del self.city

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")
