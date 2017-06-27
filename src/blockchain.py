import random
import sys
import time

from .utils import sha_256
from .block import Block


BLOCK_TIME_SEC = 1
START_DIFFICULTY = 16
MAX_DIFFICULTY = 256
DIFFICULTY_STEP_SIZE = 2

class BlockChain(object):
    def __init__(self):
        self.blockchain = []
        self.num_blocks = 0
        self.last_block_hash = 0
        self.difficulty = self._calibrate_difficulty()
        self.head = None

    def pretty_print(self):
        print()
        for block in self.blockchain:
            block.pretty_print()
            print("\t\t|")
            print("\t\tv")


    """
        Adjust difficulty until mining time approximates BLOCK_TIME_SEC
    """
    def _calibrate_difficulty(self):
        for difficulty in range(START_DIFFICULTY, MAX_DIFFICULTY, DIFFICULTY_STEP_SIZE):
            target = 2 ** (257 - difficulty) - 1
            hash_val = 2 ** (257) - 1
            nonce = random.randint(0, sys.maxsize)

            start = time.time()
            hash_val = sha_256(nonce)
            while hash_val > target:
                nonce += 1
                hash_val = sha_256(nonce)
            end = time.time()
            if(end - start) > BLOCK_TIME_SEC:
                return difficulty

    def _append_block(self, block):
        self.blockchain.append(block)
        self.num_blocks += 1

    def _drop_blocks(self):
        self.blockchain = []

    def hash_document(self, document):
        return sha_256(document)

    def validate(self):
        if self.head.parent_hash == 0:
            return True

        expected_hash = self.head.parent_hash
        for block in reversed(blockchain[1:]):
            actual_hash = hash(block.block_string)
            if expected_hash != actual_hash:
                return False

        return True

    def create_block(self, document, document_name):
        document_hash = self.hash_document(document)
        block = Block(self.last_block_hash, document_hash, document_name)
        self._append_block(block)

        self.last_block_hash = block.mine(self.difficulty)
        if not self.head:
            self.head = block
