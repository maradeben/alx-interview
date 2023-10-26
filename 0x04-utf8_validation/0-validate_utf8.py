#!/usr/bin/python3
""" UTF8 validation module """
from typing import List


def validUTF8(data: List) -> bool:
    """ validate the data, return True or False """
    following_bytes = 0

    for byte in data:
        byte = bin(byte)[2:].zfill(8)  # convert to binary, 8 bits
        if following_bytes == 0:
            if byte[0] == '0':
                continue
            elif byte.startswith('110'):
                following_bytes = 1
            elif byte.startswith('1110'):
                following_bytes = 2
            elif byte.startswith('11110'):
                following_bytes = 3
            elif binary.startswith('10'):
                return False
        else:
            if not byte.startswith('10'):
                return False
            following_bytes = -1
    return following_bytes == 0
