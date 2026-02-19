def rotate(text, key):
    ans = ''
    for char in text:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            ans += chr(start + (ord(char) - start + key) % 26)
        else:
            ans += char
    return ans