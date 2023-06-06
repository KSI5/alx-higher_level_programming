#!/usr/bin/python3
alphabet = ''.join(chr(letter) for letter in range(ord('a'), ord('z')+1) if chr(letter) not in 'qe')
print("{}".format(alphabet), end='')
