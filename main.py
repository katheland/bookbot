# BOOKBOT PROJECT
# Katherine Anderson
# Bookbot project for Boot.dev

import sys
from stats import *

# takes in a path to a text file
# reports the number of words in the document and the number of occurances of
# each letter of the alphabet
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    file_contents = open_file(path_to_file)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{num_words(file_contents)} words found in the document\n")
    print_characters(num_characters(file_contents))
    print("--- End report ---")

# opens the file and parses it to a string
def open_file(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

# format and print each line of the list of dictionaries of characters
# (but only print if it's an alphabetical character)
def print_characters(char_dict):
    for c in char_dict:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")

main()