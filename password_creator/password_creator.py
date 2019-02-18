#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import random
import sys
import argparse
from .stuff import word_set

__version__ = "1.2.0"
SPECIALS = {"!", "@", "#", "$", "%", "^", "&", "*", "("}
NUMS = set(range(1, 1000))
DEFAULT_DELIMITER = "-"
DEFAULT_NUM_WORDS = 3


def create_parser():
    """ Create argparse object for this CLI """
    parser = argparse.ArgumentParser(
        description="Create strong random passwords with ease")

    parser.add_argument("--set_length", "-st", type=int,
                        help="Set number of words in password")

    parser.add_argument(
        "--set_delimiter",
        "-sd",
        help="Set the delimiter between words to any char/string")

    parser.add_argument(
        "--set_chars",
        "--num_chars",
        "-sc",
        type=int,
        help="Set number of characters")

    parser.add_argument(
        "--with_numbers",
        "-wn",
        action="store_true",
        help="Add numbers to password")

    parser.add_argument(
        "--with_specials",
        "-ws",
        action="store_true",
        help="Add special characters to password")

    return parser


def password_creator(args, word_set):
    """
    Generate a "random" password based on words from the word set
    """
    ret = ""
    num = DEFAULT_NUM_WORDS
    delimiter = DEFAULT_DELIMITER
    chars = -1  # Go to end of string by default
    if args.set_length:
        num = int(args.set_length)
    if args.set_delimiter:
        delimiter = args.set_delimiter
    if args.set_chars:
        chars = int(args.set_chars)

    words = random.sample(word_set, num)
    for item in words:
        ret += item + delimiter
    ret = list(ret)

    num_specials = len(ret) // 10
    sample = []
    if args.with_numbers:
        sample += str(random.sample(NUMS, num_specials))

    if args.with_specials:
        sample += random.sample(SPECIALS, num_specials)

    for special in sample:
        pos = random.randint(0, len(ret) - 1)
        ret[pos] = special

    ret = ret[0:chars]
    ret = "".join(ret)
    return ret.replace("'s", "s")


def main():
    """
    Main function for running the program
    """
    parser = create_parser()
    args = parser.parse_args()
    print(password_creator(args, word_set))
