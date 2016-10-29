#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import random
import sys
from .stuff import word_set

__version__ = "0.0.1"


def password_creator(word_set):
    """
    Generate a "random" password based on words from the word set

    @param word_set: set(str)
    @return: str
    """
    returned_str = ""
    num = 3
    delimiter = "-"
    if len(sys.argv) > 1:  # Argument handling
        if "--set_length" in sys.argv and \
                represents_int(sys.argv[sys.argv.index("--set_length") + 1]):
            num = int(sys.argv[sys.argv.index("--set_length") + 1])
        if "--set_delimiter" in sys.argv:
            delimiter = (sys.argv[sys.argv.index("--set_delimiter") + 1])
    words = random.sample(word_set, num)
    for item in words:
        returned_str += item + delimiter
    return returned_str[:-1].replace("'s", "s")


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