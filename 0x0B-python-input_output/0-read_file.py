#!/usr/bin/python3

"""function that reads a text file"""


def read_file(filename=""):
    with open(filename, "r", encoding="utf8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(line, end="")
