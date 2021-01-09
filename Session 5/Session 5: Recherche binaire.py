def binary_search ( name, list_of_names ):
    first = 0
    last = len(list_of_names)-1
    found = False

    while first<=last and not found:
        middle = (first + last)//2
        if list_of_names[middle][0] == name:
            return list_of_names[middle][1]
        else:
            if name < list_of_names[middle][0]:
                last = middle-1
            else:
                first = middle+1

    return []
