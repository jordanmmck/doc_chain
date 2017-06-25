import hashlib
import random
import array
import json
import sys


"""
    Takes any arg form?
    Returns digest in int form
"""
def hash(payload):
    payload = str(payload)
    payload = payload.encode()
    hash_object = hashlib.sha256(payload)
    int_digest = int.from_bytes(hash_object.digest(),byteorder='big')
    return int_digest

class Block(object):
    def __init__(self, parent_hash, document_hash):
        self.parent_hash = parent_hash
        self.document_hash = document_hash
        self.nonce = random.randint(0, sys.maxsize)

    def _get_payload_string(self):
        block_string = '{hash}/{document_hash}/{nonce}'.format(
                        hash=str(self.parent_hash),
                        document_hash=str(self.document_hash),
                        nonce=str(self.nonce)
                    )

        return block_string

    """
        difficulty: 0-256
            0: all ones, every number is smaller than this (instant win)
            256: all zeroes, every number is larger than this (impossible to win)
            Each level is 2 times more difficult
    """
    def mine(self, difficulty):

        target = 2 ** (257 - difficulty) - 1
        hash_val = 2 ** (257) - 1

        block_string = self._get_payload_string()
        while hash_val > target:
            hash_val = hash(block_string)
            block_string = self._get_payload_string()
            self.nonce = (self.nonce + 1) % sys.maxsize

        return hash_val


class BlockChain(object):
    def __init__(self):
        self.blockchain = []
        self.num_blocks = 0
        self.last_block_hash = 0
        self.difficulty = 0

    def calibrate_difficulty(self):
        self.difficulty = 4

    def _append_block(self, block):
        self.blockchain.append(block)
        self.num_blocks += 1

    def hash_document(self, document):
        return random.randint(0,100000000000)

    def validate_blockchain(self):
        pass

    def create_block(self, document):
        document_hash = self.hash_document(document)
        block = Block(self.last_block_hash, document_hash)
        self._append_block(block)

        if self.difficulty == 0:
            self.calibrate_difficulty()

        self.last_block_hash = block.mine(3)

