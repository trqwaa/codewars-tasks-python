def divisors(n):
    count = 0
    for x in range(1, n + 1):
        if n % x == 0:
            count += 1
            
        
    return count

# range(1, n + 1) - то что переберает числа от 1 до n значения НО не выводиться, для этого нужна переменная count или любая 