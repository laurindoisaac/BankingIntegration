# test_bankingintegration.py
"""
Tests for BankingIntegration module.
"""

import unittest
from bankingintegration import BankingIntegration

class TestBankingIntegration(unittest.TestCase):
    """Test cases for BankingIntegration class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BankingIntegration()
        self.assertIsInstance(instance, BankingIntegration)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BankingIntegration()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
