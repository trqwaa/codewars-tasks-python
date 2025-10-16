def number(lines):
    new = []
    for x, letter in enumerate( lines, start= 1):
        new.append("{}: {}".format(x, letter))

    return new