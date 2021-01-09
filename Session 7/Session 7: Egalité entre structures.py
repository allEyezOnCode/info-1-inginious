def equal(l, d):
    for x, line in enumerate(l):
        for y, value in enumerate(line):
            if ((x, y) not in d and value != 0) or (value != 0 and d[(x, y)] != value):
                return False
    return True
                
