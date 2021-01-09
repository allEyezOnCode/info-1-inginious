def marks_from_file(filename):
    with open(filename) as f: lines = f.readlines()
    return [Student(line.split()[0], line.split()[1], int(line.split()[2].strip())) for line in lines]
