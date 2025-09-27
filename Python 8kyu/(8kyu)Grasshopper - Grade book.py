def get_grade(s1, s2, s3):
    note = (s1 + s2 + s3) / 3
    if note >= 90 and note <= 100:
        return "A"
    elif note >= 80 and note <= 90:
        return "B"
    elif note >= 70 and note <= 80:
        return "C"
    elif note >= 60 and note <= 70:
        return "D"
    else:
        return "F"
    