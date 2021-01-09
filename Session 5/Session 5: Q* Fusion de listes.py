i = 0
res = []
for el in first_list:
    while  i < len(second_list) and second_list[i][1] <= el[1]:
        res.append(second_list[i])
        i += 1
    res.append(el)
if i < len(second_list):
    res.extend(second_list[i:])
return res
