def create_dict(l):
    new_dict = {}
    for el in l:
        if el[0] in new_dict:
            new_dict[el[0]].append(el[1])
        else:
            new_dict[el[0]] = [el[1]]
    return new_dict
