def score(x, y):
    dis = (x ** 2 + y ** 2) ** 0.5
    if dis <= 1:
        return 10
    if dis <= 5:
        return 5
    if dis <= 10:
        return 1
    return 0
