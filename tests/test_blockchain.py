import unittest

from src.blockchain import BlockChain
from src.block import Block
from src.utils import sha_256


class test_blockchain(unittest.TestCase):

    def setUp(self):
        self.sample_blockchain = BlockChain(1)

    def test_create_genesis_block(self):
        # act
        self.sample_blockchain.create_block(123123123, 'doc1')

        # assert
        # if the blockchain is empty then first block has prev of 0, not addr passed in
        self.assertEqual(self.sample_blockchain.blockchain[0].parent_hash, 0)

    def test_create_non_genesis_block(self):
        # arrange
        self.sample_blockchain.create_block(123123123, 'doc1')

        # act
        self.sample_blockchain.create_block(456456456, 'doc2')

        # assert
        hash_of_first_block = sha_256(self.sample_blockchain.blockchain[0].block_string)
        self.assertEqual(self.sample_blockchain.blockchain[1].parent_hash, hash_of_first_block)

    def test_validate_blockchain(self):
        # arrange
        self.sample_blockchain.create_block(123123123, 'doc1')
        self.sample_blockchain.create_block(456456456, 'doc2')

        # act, assert
        self.assertTrue(self.sample_blockchain.validate())


