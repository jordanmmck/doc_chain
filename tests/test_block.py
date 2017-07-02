import unittest
from src.blockchain import BlockChain
from src.block import Block

from src.utils import sha_256


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


