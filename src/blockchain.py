from .utils import sha_256
from .block import Block


class BlockChain(object):
    def __init__(self, difficulty):
        self.blockchain = []
        self.num_blocks = 0
        self.last_block_hash = 0
        self.difficulty = difficulty
        self.head = None

    def pretty_print(self):
        print()
        for block in self.blockchain:
            block.pretty_print()
            print("\t\t|")
            print("\t\tv")

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
