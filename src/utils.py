import hashlib


"""
    Takes any arg form?
    Returns digest in int form
"""
def sha_256(payload):
    payload = str(payload)
    payload = payload.encode()
    hash_object = hashlib.sha256(payload)
    int_digest = int.from_bytes(hash_object.digest(),byteorder='big')
    return int_digest
