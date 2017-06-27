import sys

from .blockchain import BlockChain
from .utils import calibrate_difficulty


difficulty = calibrate_difficulty()
blockchain = BlockChain(difficulty)

doc_list = sys.argv[1:]
for doc in doc_list:
    f = open(doc, "rb")
    data = f.read()
    blockchain.create_block(data, doc)
    f.close()

blockchain.pretty_print()
