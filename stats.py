def sort_on(dict):
    return dict["num"]

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