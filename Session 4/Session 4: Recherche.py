def recherche(m, v):
    for row in m:
        if v in row:
            return True
    return False
