import re

def translate_word(word):
    if word.startswith(('a', 'e', 'i', 'o', 'u', 'xr', 'yt')):
        return word + "ay"
    
    match = re.match(r'^([^aeiou]*qu)(.*)', word)
    if match:
        return match.group(2) + match.group(1) + "ay"
    
    match = re.match(r'^([^aeiou]+)(y.*)', word)
    if match:
        return match.group(2) + match.group(1) + "ay"
    
    match = re.match(r'^([^aeiou]+)(.*)', word)
    if match:
        return match.group(2) + match.group(1) + "ay"
        
    return word

def translate(text):
    return " ".join(translate_word(word) for word in text.split())