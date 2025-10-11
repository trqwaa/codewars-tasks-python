def create_phone_number(n):
    a = ''.join(str(x) for x in n[0:3])
    b = ''.join(str(x) for x in n[3:6])
    c = ''.join(str(x) for x in n[6:10])
    result = '({}) {}-{}'.format(a, b, c)
    return result

