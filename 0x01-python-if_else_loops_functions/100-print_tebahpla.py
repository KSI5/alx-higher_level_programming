#!/usr/bin/python3

"""Print the alphabet in reverse order alternating uppercase and lowercase."""

for c in range(ord('z'), ord('a') - 1, -1):
    if (ord('z') - c) % 2 == 0:
        print(chr(c), end="")
    else:
        print(chr(c).upper(), end="")
