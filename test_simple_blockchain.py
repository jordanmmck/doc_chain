import unittest
from simple_blockchain import Block, BlockChain, sha256


class test_block(unittest.TestCase):

    def setUp(self):
        self.sample_block = Block('0x123fff', 123123123, 'my_doc')

    def test_mine_hash_val_less_than_target(self):
        # arrange
        difficulty = 3

        # act
        hash_val = self.sample_block.mine(difficulty)

        # assert
        assert hash_val < 2**(257-difficulty)-1

class test_blockchain(unittest.TestCase):

    def setUp(self):
        self.sample_blockchain = BlockChain()


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
        hash_of_first_block = sha256(self.sample_blockchain.blockchain[0].block_string)
        self.assertEqual(self.sample_blockchain.blockchain[1].parent_hash, hash_of_first_block)

    def test_validate_blockchain(self):
        # arrange
        self.sample_blockchain.create_block(123123123, 'doc1')
        self.sample_blockchain.create_block(456456456, 'doc2')
        # print(self.sample_blockchain)
        print(self.sample_blockchain.pretty_print())

        # act, assert
        self.assertTrue(self.sample_blockchain.validate())

class test_document_order_of_existence(unittest.TestCase):
    pass
