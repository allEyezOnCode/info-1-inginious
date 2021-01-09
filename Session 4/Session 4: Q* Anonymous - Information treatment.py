def treatment(data):
    line = data.split()
    current = None
    res = ""
    occ = 0
    for word in line:
        if current is None:
            current = word
            occ = 1
        elif word != current:
            res += current + '*' + str(occ) + ' '
            current = word
            occ = 1
        else:
            occ += 1
    res += current + '*' + str(occ)
    return res
