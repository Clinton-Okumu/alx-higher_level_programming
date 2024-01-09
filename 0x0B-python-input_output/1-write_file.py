#!/usr/bin/python3

"""function writing string to text file"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf8") as file:
        nb_characters = file.write(text)
    return nb_characters
