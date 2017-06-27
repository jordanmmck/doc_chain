import hashlib
import random
import sys
import time


"""
    Returns digest in int form
"""
def sha_256(payload):
    payload = str(payload)
    payload = payload.encode()
    hash_object = hashlib.sha256(payload)
    int_digest = int.from_bytes(hash_object.digest(),byteorder='big')
    return int_digest

BLOCK_TIME_SEC = 1
START_DIFFICULTY = 1
MAX_DIFFICULTY = 256
DIFFICULTY_STEP_SIZE = 1

"""
    Adjust difficulty until mining time approximates BLOCK_TIME_SEC
"""
def calibrate_difficulty():
    # for testing
    # return 1
    print("starting calibration...")
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

