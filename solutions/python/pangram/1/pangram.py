import string


def is_pangram(sentence):
    return all(c in sentence.lower() for c in string.ascii_lowercase)
