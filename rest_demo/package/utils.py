import hashlib


def hash_md5(input_string):
    return hashlib.md5(input_string.encode()).hexdigest()
