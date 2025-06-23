#!/usr/bin/python3
def uppercase(str):
    for c in str:
        # Convert lowercase letter to uppercase by subtracting 32 from ASCII code
        if 'a' <= c <= 'z':
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print("{}".format(c), end="")
    print()
