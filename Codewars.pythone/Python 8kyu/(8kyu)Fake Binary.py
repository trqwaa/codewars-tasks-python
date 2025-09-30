def fake_bin(x):
    result = ''
    for num in x:
        n = int(num)
        if n < 5:
            result += "0"
        else:
            result += "1"

    return result