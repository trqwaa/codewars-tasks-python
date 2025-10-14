def disemvowel(string_):
    vowels = 'aeiouAEIOU'
    text = ''
    for x in string_:
        if x not in vowels:
            text += x
    return text