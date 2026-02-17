def response(hey_bob):
    phrase = hey_bob.strip()
    
    if not phrase:
        return "Fine. Be that way!"
        
    is_shouting = phrase.isupper()
    is_question = phrase.endswith("?")
    
    if is_shouting and is_question:
        return "Calm down, I know what I'm doing!"
    if is_shouting:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
    return "Whatever."