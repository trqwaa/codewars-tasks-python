def accum(st):
    result_list = []
    for x, letter in enumerate(st, start=1):
        y = letter.upper() + letter.lower() * (x-1)
        result_list.append(y)
    pass
    result = '-'.join(result_list)
    return print (accum(123))


#для такого идиота это было сложновато

# enumerate - это функция, которая перебирает элементы последовательности и одновременно даёт их индексы.