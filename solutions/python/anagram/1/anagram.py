def find_anagrams(word, candidates):
    return [c for c in candidates if word.lower() != c.lower() and sorted(word.lower()) == sorted(c.lower())]