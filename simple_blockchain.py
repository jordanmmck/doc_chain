import hashlib
import random
import array
import json


class block(object):
    def __init__(self, parent_hash, transactions_list, nonce):
        self.parent_hash = parent_hash
        self.transactions_list = transactions_list
        self.nonce = nonce

    def _get_payload_string(self):
        block_string = '{hash}/{transactions}/{nonce}'.format(
                        hash=str(self.parent_hash),
                        transactions=''.join(self.transactions_list),
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

        target = 2**(257-difficulty)-1
        hash_val = 2**(257)-1

        block_string = self._get_payload_string()
        while hash_val > target:
            payload = block_string.encode()
            hash_object = hashlib.sha256(payload)
            hash_val = int.from_bytes(hash_object.digest(),byteorder='big')
            block_string = self._get_payload_string()
            self.nonce += 1

        return hash_val


# print(hash_val.zfill(32))
# print(target.zfill(32))

# gets a string
# hash_val = hash_object.hexdigest()
# prints an int
# print(int.from_bytes(hash_object.digest(), byteorder='big'))
