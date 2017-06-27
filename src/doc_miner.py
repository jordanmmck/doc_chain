from .blockchain import BlockChain


class DocumentOrderOfExistence(object):
    def __init__(self):
        self.blockchain = BlockChain()
        self.document_count = 0

    def find_doc_position(self, document):
        pass

    def get_full_doc_ordering(self):
        pass
