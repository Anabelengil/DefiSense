# test_defisense.py
"""
Tests for DefiSense module.
"""

import unittest
from defisense import DefiSense

class TestDefiSense(unittest.TestCase):
    """Test cases for DefiSense class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = DefiSense()
        self.assertIsInstance(instance, DefiSense)

    def test_run_method(self):
        """Test the run method."""
        instance = DefiSense()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
