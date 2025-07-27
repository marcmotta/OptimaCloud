# test_optimacloud.py
"""
Tests for OptimaCloud module.
"""

import unittest
from optimacloud import OptimaCloud

class TestOptimaCloud(unittest.TestCase):
    """Test cases for OptimaCloud class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OptimaCloud()
        self.assertIsInstance(instance, OptimaCloud)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OptimaCloud()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
