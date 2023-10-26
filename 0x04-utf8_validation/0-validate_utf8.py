#!/usr/bin/python3
""" UTF8 validation module """
from typing import List


def validUTF8(data: List) -> bool:
    """ validate the data, return True or False """
    def is_continuation(byte):
        """
        is it a continuation?
        Args:
            byte (byte)
        Returns:
            returns a bool
        """
        return (byte & 0b11000000) == 0b10000000

    def get_bytes_to_follow(start_byte):
        """
        Get the bytes to follow
        Args:
            start_byte (byte): Where to start
        Returns:
            returns an int
        """
        if (start_byte & 0b10000000) == 0b00000000:
            return 0
        elif (start_byte & 0b11100000) == 0b11000000:
            return 1
        elif (start_byte & 0b11110000) == 0b11100000:
            return 2
        elif (start_byte & 0b11111000) == 0b11110000:
            return 3
        return -1
    bytes_to_follow = 0

    for byte in data:
        if bytes_to_follow == 0:
            bytes_to_follow = get_bytes_to_follow(byte)
            if bytes_to_follow == -1:
                return False
            elif bytes_to_follow == 0:
                continue
        else:
            if not is_continuation(byte):
                return False
            bytes_to_follow -= 1
    return bytes_to_follow == 0
