# test_blockchainnftvaultmanagerlabsnext.py
"""
Tests for BlockchainNFTVaultManagerLabsNext module.
"""

import unittest
from blockchainnftvaultmanagerlabsnext import BlockchainNFTVaultManagerLabsNext

class TestBlockchainNFTVaultManagerLabsNext(unittest.TestCase):
    """Test cases for BlockchainNFTVaultManagerLabsNext class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockchainNFTVaultManagerLabsNext()
        self.assertIsInstance(instance, BlockchainNFTVaultManagerLabsNext)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockchainNFTVaultManagerLabsNext()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
