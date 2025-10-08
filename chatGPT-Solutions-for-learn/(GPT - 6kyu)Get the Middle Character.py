def Middle_Character(s):
    y = len(s) // 2
    if len(s) % 2:
        return s[y]
    else:
        return s[y-1:y+1]
    