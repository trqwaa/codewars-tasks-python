def count_positives_sum_negatives(arr):
    x = 0
    y = 0
    if arr is None or len(arr) == 0:
        return []
    else:
        for num in arr:
            if num > 0: 
                x = x + 1
            else:
                y = y + num
  
        return [x, y]
    