def find_short(s):
    l = s.split()
    short = len(l[0])
    for x in l:
        if short > len(x):
            short = len(x)
        else:
            None
        
    return short