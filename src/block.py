import random
import sys

from .utils import sha_256


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
        hash_val = sha_256(block_string)
        while hash_val > target:
            nonce = (nonce + 1) % sys.maxsize
            block_string = self.block_string + str(nonce)
            hash_val = sha_256(block_string)

        self.block_string = block_string
        self.final_nonce = nonce
        return hash_val
