def is_valid(isbn):
    isbn = isbn.replace('-', '')

    if len(isbn) != 10:
        return False

    if not isbn[:9].isdigit():
        return False

    if not (isbn[9].isdigit() or isbn[9] == 'X'):
        return False
    
    total, start = 0, 10
    for char in isbn:
        total += (10 if char == 'X' else int(char)) * start
        start -= 1
    return total % 11 == 0
