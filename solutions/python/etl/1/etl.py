def transform(legacy_data):
    ans = {}
    for socre, letters in legacy_data.items():
        for letter in letters:
            ans[letter.lower()] = socre
    return ans