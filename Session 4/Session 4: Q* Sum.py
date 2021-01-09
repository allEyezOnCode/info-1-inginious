s = 0
for el in list:
    if isinstance(el, int) or isinstance(el, float):
        s += el
return s
