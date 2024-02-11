#!/usr/bin/python3
"""Unit test for Review class"""
import unittest
import os
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def setUp(self):
        """Setup method"""
        self.review = Review()

    def tearDown(self):
        """Teardown method"""
        del self.review

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

