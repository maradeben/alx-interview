#!/usr/bin/python3
""" UTF8 validation module """
from typing import List


def validUTF8(data: List) -> bool:
    """ validate the data, return True or False """
    # check if first byte is valid
    first_byte = data[0]
    if first_byte < 0 or first_byte > 255:
        return False

    # track continuation bytes
    expected_continuation_bytes = 0

    # looop over each byte
    for byte in data:
        # check valid continuation byte
        if expected_continuation_bytes > 0:
            if byte < 128 or byte > 191:
                return False
            expected_continuation_bytes -= 1
        # check valid new character byte start
        else:
            if byte < 128:
                continue
            elif byte < 192:
                expected_continuation_bytes = 1
            elif byte < 224:
                expected_continuation_bytes = 2
            elif byte < 240:
                expected_continuation_bytes = 3
            else:
                # Invalid start byte.
                return False

    if expected_continuation_bytes > 0:
        return False

    return True
