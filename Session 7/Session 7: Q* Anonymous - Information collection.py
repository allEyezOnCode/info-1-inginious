def collect(file):
    dic = {}
    with open(file) as f: lines = f.read().splitlines()
    for line in lines:
        pattern = treatment(extract(line))
        dic[pattern] = dic.get(pattern, 0) + 1
    return dic
