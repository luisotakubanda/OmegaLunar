# test_omegalunar.py
"""
Tests for OmegaLunar module.
"""

import unittest
from omegalunar import OmegaLunar

class TestOmegaLunar(unittest.TestCase):
    """Test cases for OmegaLunar class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OmegaLunar()
        self.assertIsInstance(instance, OmegaLunar)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OmegaLunar()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
