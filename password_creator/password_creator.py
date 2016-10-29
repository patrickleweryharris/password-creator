#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import random
import sys
from .stuff import word_set

__version__ = "1.1.0"
special_chars = {"!", "@", "#", "$", "%", "^", "&", "*", "("}
numbers = set(range(1, 1000))


def password_creator(word_set):
    """
    Generate a "random" password based on words from the word set

    @param word_set: set(str)
    @return: str
    """
    returned_str = ""
    num = 3  # Default number of words is 3, default delimiter is the dash
    delimiter = "-"
    chars = -1
    if len(sys.argv) > 1:  # Argument handling
        if "--set_length" in sys.argv and \
                represents_int(sys.argv[sys.argv.index("--set_length") + 1]):
            num = int(sys.argv[sys.argv.index("--set_length") + 1])
        if "--set_delimiter" in sys.argv:
            delimiter = sys.argv[sys.argv.index("--set_delimiter") + 1]
        if "--set_chars" in sys.argv and \
                represents_int(sys.argv[sys.argv.index("--set_chars") + 1]):
            chars = int(sys.argv[sys.argv.index("--set_chars") + 1])
    words = random.sample(word_set, num)
    for item in words:
        returned_str += item + delimiter
    middle = len(returned_str)//2
    if "--with_numbers" in sys.argv:
        returned_str = returned_str[:middle] + str((random.sample(numbers, 1)[0])) + returned_str[middle:]
        middle += 1
    if "--with_specials" in sys.argv:
        returned_str = returned_str[:middle] + random.sample(special_chars, 1)[0] + returned_str[middle:]
        middle += 1
    return returned_str[0:chars].replace("'s", "s")


def represents_int(s):
    """
    Check if str s represents a valid int

    Used for input sanitization

    @param s: str
    @return: bool
    """
    try:
        int(s)
        return True
    except ValueError:
        return False


def main():
    """
    Main function for running the program
    """
    print(password_creator(word_set))
