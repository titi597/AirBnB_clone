#!/usr/bin/python3
"""Unit test for Amenity class"""
import unittest
import os
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def setUp(self):
        """Setup method"""
        self.amenity = Amenity()

    def tearDown(self):
        """Teardown method"""
        del self.amenity

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "")
