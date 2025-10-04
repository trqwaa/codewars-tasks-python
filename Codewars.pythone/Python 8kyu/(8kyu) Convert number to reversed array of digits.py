def digitize(n):
    n = str(n)
    y = list(n)
    u = y[::-1]
    i = [int(x) for x in u]
    return i