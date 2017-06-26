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
    def __init__(self, parent_hash, document_hash, document_name):
        self.parent_hash = parent_hash
        self.document_hash = document_hash
        self.document_name = document_name
        self.final_nonce = None
        self.block_string = '{parent_hash}/{document_hash}/'.format(
            parent_hash=str(self.parent_hash),
            document_hash=str(self.document_hash)
        )

    def pretty_print(self):
        block = (
                " \t{top_border}\n"
                "\t| HEADER  : 0x{header:064x}\n"
                "\t| DOC_NAME: {doc_name}\n"
                "\t| DOC_HASH: 0x{doc_hash:064x}\n"
                "\t| NONCE   : 0x{nonce:064x}\n"
                "\t{bottom_border}\n".format( 
                        top_border='-'*80,
                        header=self.parent_hash,
                        doc_name=self.document_name,
                        doc_hash=self.document_hash,
                        nonce=self.final_nonce,
                        bottom_border='-'*80
                    )
                )
        print(block)

    """
        difficulty: 0-256
            0: all ones, every number is smaller than this (insta mine)
            256: all zeroes, every number is larger than this (impossible to mine)
            Each level is more difficult by a factor of 2
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
        self.final_nonce = nonce
        return hash_val


class BlockChain(object):
    def __init__(self):
        self.blockchain = []
        self.num_blocks = 0
        self.last_block_hash = 0
        self.difficulty = 0
        self.head = None

    def pretty_print(self):
        print()
        for block in self.blockchain:
            block.pretty_print()
            print("\t\t|")
            print("\t\tv")

    def calibrate_difficulty(self):
        self.difficulty = 14

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

    def create_block(self, document, document_name):
        document_hash = self.hash_document(document)
        block = Block(self.last_block_hash, document_hash, document_name)
        self._append_block(block)

        if self.difficulty == 0:
            self.calibrate_difficulty()

        self.last_block_hash = block.mine(self.difficulty)
        if not self.head:
            self.head = block


class DocumentOrderOfExistence(object):
    def __init__(self):
        self.blockchain = BlockChain()
        self.document_count = 0

    def find_doc_position(self, document):
        pass

    def get_full_doc_ordering(self):
        pass
