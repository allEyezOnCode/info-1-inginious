def house_designation(student_qualities):
    student_qualities = set(student_qualities)
    dic = {}
    for house, qualities in knowledge:
        dic[house] = len(student_qualities.intersection(qualities))
    return list(dict(sorted(dic.items(), key=lambda x: x[1], reverse=True)).keys())
