#!/usr/bin/python3

alphabet = ""
for letter in range(ord('a'), ord('z')+1):
    if chr(letter) not in 'eq':
        alphabet += chr(letter)

print("{}".format(alphabet), end="")

