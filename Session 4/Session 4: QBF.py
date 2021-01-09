def positions(p, s):
    occ_lst = []
    p = p.lower()
    s = s.lower()
    for i, char in enumerate(s[:-len(p)+1]):
        if is_occ(i, s, p):
            occ_lst.append(i)
    return occ_lst

def is_occ(index, s, pattern):
    for i, char in enumerate(pattern):
        if s[index+i] != char and char != '?':
            return False
    return True
