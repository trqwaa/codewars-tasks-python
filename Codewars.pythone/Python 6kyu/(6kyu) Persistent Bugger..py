def persistence(n):
    
    if n < 10:
        return 0

    result_count = 0

    while n >= 10:
        product = 1
        for num in str(n):
            product *= int(num)
        n = product
        result_count += 1

    return result_count

