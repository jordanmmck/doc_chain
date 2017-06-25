import unittest
from simple_blockchain import block


class testSimpleBlock(unittest.TestCase):

    def setUp(self):
        self.sample_block = block('0x123fff', ['t0', 't1', 't2'], 0)

    def test_mine_hash_val_less_than_target(self):
        # arrange
        difficulty = 3

        # act
        hash_val = self.sample_block.mine(difficulty)

        # assert
        assert hash_val < 2**(257-difficulty)-1

class testSimpleBlockchain(unittest.TestCase):

    def setUp(self):
        self.sample_block = block('0x123fff', ['t0', 't1', 't2'], 0)

    def test_mine_hash_val_less_than_target(self):
        # arrange
        difficulty = 3

        # act
        hash_val = self.sample_block.mine(difficulty)

        # assert
        assert hash_val < 2**(257-difficulty)-1
