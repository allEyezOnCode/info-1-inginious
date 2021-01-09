def write_coordinates(filename, l):
    with open(filename, 'w') as f:
        for i, el in enumerate(l):
            f.write(f'{el[0]},{el[1]}')
            if i != len(l) - 1:
                f.write('\n')
def read_coordinates(filename):
    res = []
    with open(filename) as f:
        for line in f:
            res.append(tuple(map(float, line.split(','))))
    return res
