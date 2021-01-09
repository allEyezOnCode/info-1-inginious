def create_dictionary(filename):
    with open(filename) as f:
        dictionary = {}
        for line in f:
            for word in line.split(" "):
                dictionary[word] = dictionary.get(word, 0) + 1
    return dictionary
def occ(dictionary, word):
    return dictionary.get(word, 0)
