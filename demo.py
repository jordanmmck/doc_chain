from src.blockchain import BlockChain

print('Creating blockchain')
print('Adjusting difficulty...')

blockchain = BlockChain()
print('Difficulty: ' + str(blockchain.difficulty))

document_1 = 123123123123123
blockchain.create_block(document_1, 'document_1')
print('block 1 mined...')
# blockchain.head.pretty_print()

document_2 = 234234234234234
blockchain.create_block(document_2, 'document_2')
print('block 2 mined...')
# blockchain.head.pretty_print()

document_3 = 345345345345345
blockchain.create_block(document_3, 'document_3')
print('block 3 mined...')
# blockchain.head.pretty_print()

document_4 = 456456456456456
blockchain.create_block(document_4, 'document_4')
print('block 4 mined...')
# blockchain.head.pretty_print()

blockchain.pretty_print()
