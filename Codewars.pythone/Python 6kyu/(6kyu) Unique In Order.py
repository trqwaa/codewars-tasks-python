def unique_in_order(sequence):
    list_new = []
    if not sequence:
        return []
    list_new.append(sequence[0])
    for x in sequence[1:]:
        if x != list_new[-1]:
            list_new.append(x)
            
    return list_new