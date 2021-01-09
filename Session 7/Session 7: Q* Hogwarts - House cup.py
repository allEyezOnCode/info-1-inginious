houses = ["gryffindor", "ravenclaw", 'hufflepuff', 'slytherin']
def winning_house(scroll):
    score = [0, 0, 0, 0]
    with open(scroll) as f: lines = f.readlines()
    for line in lines:
        for i, house in enumerate(houses):
            if line.split(" ")[0] in students[house]:
                score[i] = score[i] + int(line.split(" ")[1].strip())
    best = [houses[i] for i, result in enumerate(score) if result == max(score)]
    if len(best) == 1: return best[0]
    return best
