def find_outlier(integers):
    neCHOT = []
    chot =  []

    for x in integers[0:3]:
        if x % 2 == 0:
            chot.append(x)
        else:
            neCHOT.append(x)

    if len(chot) > len(neCHOT):
        for x in integers:
            if x % 2 != 0:
                return x
    
    else:
        for x in integers:
            if x % 2 == 0:
                return x
            
# ДАААААААААААААААААААААААААААААААААААААААААААААААААААААААААА