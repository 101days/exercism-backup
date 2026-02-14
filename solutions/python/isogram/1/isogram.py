def is_isogram(string):
    s = set()
    for c in string.lower():
        if c.isalpha():
            if c in s:
                return False
            s.add(c)
    return True