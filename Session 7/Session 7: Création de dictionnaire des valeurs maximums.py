def create_dict_max(l):
    l = sorted(l)
    return {el[0]:el[1] for el in l}
