#!/usr/bin/python3
"""Unit test for State class"""
import unittest
import os
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def setUp(self):
        """Setup method"""
        self.state = State()

    def tearDown(self):
        """Teardown method"""
        del self.state

    def test_attributes(self):
        """Test attributes"""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, "")
