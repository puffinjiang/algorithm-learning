import random
import sys

import mmh3

BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode(num, alphabet):
    """Encode a positive number into Base X and return the string.

    Arguments:
    - `num`: The number to encode
    - `alphabet`: The alphabet to use for encoding
    """
    if num == 0:
        return alphabet[0]
    arr = []
    arr_append = arr.append  # Extract bound-method for faster access.
    base = len(alphabet)
    while num:
        num, rem = divmod(num, base)
        arr_append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


def check_and_generate_key(url):
    hash_number = mmh3.hash(url)
    key = get_key_by_number(hash_number)
    # todo check key if exists
    if key:
        return key
    url = random.choice(url)
    return check_and_generate_key(url)


def get_key_by_number(hash_number):
    key = encode(hash_number, BASE62)
    max_key_len = 6
    if len(key) <= max_key_len:
        return key
    hash_number = hash_number % (pow(len(BASE62), max_key_len))
    return get_key_by_number(hash_number)


if __name__ == '__main__':
    code = mmh3.hash(
        "https://www.baidu.com/aaaaaaa/bbbbbbbds/sdffdsg/dfgdfhgdshdg/ashh/sjfgsjgjf/kgjfgh/dgfdsfgdfhfhgd")
    print(f"mmh3 code: {code}, type: {type(code)}")
    # res = encode(code & sys.maxsize,BASE62)
    print(f"res: {encode(abs(code), BASE62)}")
