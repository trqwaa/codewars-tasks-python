def order(sentence):
    wort = {
        
    }
    words = sentence.split()
    result = []
    for x in words:
        for ch in x:
            if ch.isdigit():
                wort[int(ch)] = x
    sortedKeys = sorted(wort.keys())
    for k in sortedKeys:
        result.append(wort[k])
        
    return " ".join(result)