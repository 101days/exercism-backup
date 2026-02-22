def rotate(text, key):
    ans = ""
    for t in text:
        if t.isalpha():
            r = 65 if t.isupper() else 97
            ans += chr(r + (ord(t) - r + key) % 26)
        else:
            ans += t
    return ans
