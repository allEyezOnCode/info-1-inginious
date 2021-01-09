def maximum_index(lst):
    index = None
    great = None
    for i, val in enumerate(lst):
        if great is None or val > great:
            index = i
            great = val
    return index
