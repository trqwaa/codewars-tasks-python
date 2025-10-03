def odd_or_even(arr):
        y = sum(arr)
        if y % 2 == 0:
            return ('even')
        elif y % 2 != 0:
            return ('odd')
        else:
            return [0]

