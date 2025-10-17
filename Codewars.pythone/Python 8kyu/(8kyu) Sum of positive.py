def positive_sum(arr):
    for x in arr:
        if x < 0:
            del x 
    
    return sum(x for x in arr if x > 0)
