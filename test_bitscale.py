# test_bitscale.py
"""
Tests for BitScale module.
"""

import unittest
from bitscale import BitScale

class TestBitScale(unittest.TestCase):
    """Test cases for BitScale class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BitScale()
        self.assertIsInstance(instance, BitScale)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BitScale()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
