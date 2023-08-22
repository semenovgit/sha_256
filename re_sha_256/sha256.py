import hashlib


def calculate_sha256_hash(inputstring):
    sha256_hash = hashlib.sha256(inputstring.encode()).hexdigest()
    return sha256_hash
