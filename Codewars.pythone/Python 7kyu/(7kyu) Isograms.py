def is_isogram(string):
    popa = set()
    for letter in string.lower():
        if letter in popa: 
           return False
        else:
            popa.add(letter)
            
    return True
            
    