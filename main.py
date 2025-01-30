# BOOKBOT PROJECT
# Katherine Anderson
# Bookbot project for Boot.dev

def sort_on(dict):
    return dict["num"]

# takes in a path to a text file
# reports the number of words in the document and the number of occurances of
# each letter of the alphabet
def main(path_to_file):
    file_contents = open_file(path_to_file)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{num_words(file_contents)} words were found in the document\n")
    print_characters(num_characters(file_contents))
    print("--- End report ---")

# opens the file and parses it to a string
def open_file(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

# returns the number of words in the file
def num_words(file_contents):
    words = file_contents.split()
    return len(words)

# returns a list of dictionaries of how many instances of each character
# sorted by number of instances from highest to lowest
def num_characters(file_contents):
    lower_case = file_contents.lower()

    # first split them into one dictionary
    characters = {}
    for character in lower_case:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
            
    # then split them into separate dictionaries
    # (there's probably a better way to do this...)
    chars = []
    for c in characters:
        d = {"char": c, "num": characters[c]}
        chars.append(d)
    chars.sort(reverse=True, key=sort_on)
    return chars

# format and print each line of the list of dictionaries of characters
# (but only print if it's an alphabetical character)
def print_characters(char_dict):
    for c in char_dict:
        if c["char"].isalpha():
            print(f"The '{c["char"]}' character was found {c["num"]} times")

main("books/frankenstein.txt")