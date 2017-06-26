import hashlib
import random
import sys


"""
    Takes any arg form?
    Returns digest in int form
"""
def sha256(payload):
    payload = str(payload)
    payload = payload.encode()
    hash_object = hashlib.sha256(payload)
    int_digest = int.from_bytes(hash_object.digest(),byteorder='big')
    return int_digest

class Block(object):
    def __init__(self, parent_hash, document_hash):
        self.parent_hash = parent_hash
        self.document_hash = document_hash
        self.block_string = '{parent_hash}/{document_hash}/'.format(
            parent_hash=str(self.parent_hash),
            document_hash=str(self.document_hash)
        )

    def __repr__(self):
        return self.block_string

    """
        difficulty: 0-256
            0: all ones, every number is smaller than this (instant win)
            256: all zeroes, every number is larger than this (impossible to win)
            Each level is 2 times more difficult
    """
    def mine(self, difficulty):
        target = 2 ** (257 - difficulty) - 1
        hash_val = 2 ** (257) - 1
        nonce = random.randint(0, sys.maxsize)

        # set block string with initial nonce and hash it
        block_string = self.block_string + str(nonce)
        hash_val = sha256(block_string)
        while hash_val > target:
            nonce = (nonce + 1) % sys.maxsize
            block_string = self.block_string + str(nonce)
            hash_val = sha256(block_string)

        self.block_string = block_string
        return hash_val


class BlockChain(object):
    def __init__(self):
        self.blockchain = []
        self.num_blocks = 0
        self.last_block_hash = 0
        self.difficulty = 0
        self.head = None

    def calibrate_difficulty(self):
        self.difficulty = 4

    def _append_block(self, block):
        self.blockchain.append(block)
        self.num_blocks += 1

    def _drop_blocks(self):
        self.blockchain = []

    def hash_document(self, document):
        return sha256(document)

    def validate(self):
        if self.head.parent_hash == 0:
            return True

        expected_hash = self.head.parent_hash
        for block in reversed(blockchain[1:]):
            actual_hash = hash(block.block_string)
            if expected_hash != actual_hash:
                return False

        return True

    def create_block(self, document):
        document_hash = self.hash_document(document)
        block = Block(self.last_block_hash, document_hash)
        self._append_block(block)

        if self.difficulty == 0:
            self.calibrate_difficulty()

        self.last_block_hash = block.mine(3)
        if not self.head:
            self.head = block

