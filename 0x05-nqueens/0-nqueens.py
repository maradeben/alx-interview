#!/usr/bin/python3
""" solve the nqueens challenge """
import sys


args = sys.argv
N = int(args[1])

if len(args) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

if not isinstance(N, int):
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)
