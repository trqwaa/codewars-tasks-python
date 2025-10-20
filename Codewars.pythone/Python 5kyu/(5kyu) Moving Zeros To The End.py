def move_zeros(lst):
    y = []
    lisst = []
    for x in lst:
        if x == 0:
            y.append(x)
        else: 
            lisst.append(x)
    answer = lisst + y
    return answer