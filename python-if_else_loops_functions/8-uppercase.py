#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        char = str[i]
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()
