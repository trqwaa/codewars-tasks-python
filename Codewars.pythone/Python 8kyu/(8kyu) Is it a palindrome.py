def is_palindrome(s):
    x = s[::-1]
    s = s.lower()
    x = x.lower()
    if x == s:
        return True
    
    return False
    