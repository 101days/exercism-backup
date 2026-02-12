def is_armstrong_number(number):
    res = 0
    for i in str(number):
        res += int(i) ** len(str(number))
    return res == number
