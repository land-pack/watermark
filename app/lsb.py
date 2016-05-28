import sys
import struct
import numpy
import matplotlib.pyplot as plt

from PIL import Image

from crypt import AESCipher


# Decompose a binary file into an array of bits
def decompose(data):
    v = []

    # Pack file len in 4 bytes
    fSize = len(data)
    bytes = [ord(b) for b in struct.pack("i", fSize)]

    bytes += [ord(b) for b in data]

    for b in bytes:
        for i in range(7, -1, -1):
            v.append((b >> i) & 0x1)

    return v


# Assemble an array of bits into a binary file
def assemble(v):
    bytes = ""

    length = len(v)
    for idx in range(0, len(v) / 8):
        byte = 0
        for i in range(0, 8):
            if (idx * 8 + i < length):
                byte = (byte << 1) + v[idx * 8 + i]
        bytes = bytes + chr(byte)

    payload_size = struct.unpack("i", bytes[:4])[0]

    return bytes[4: payload_size + 4]


# Set the i-th bit of v to x
def set_bit(n, i, x):
    mask = 1 << i
    n &= ~mask
    if x:
        n |= mask
    return n
