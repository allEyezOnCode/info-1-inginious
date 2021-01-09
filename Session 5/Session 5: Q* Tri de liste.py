for i, el in enumerate(a_list):
    for i2, el2 in enumerate(a_list[:-1]):
        if el2 > a_list[i2+1]:
            a_list[i2], a_list[i2+1] = a_list[i2+1], a_list[i2]
sorted_list = a_list[:]
