def referee(score_file):
    with open(score_file) as f: lines = f.readlines()
    team_1, team_2 = lines[0].strip(), lines[1].strip()
    score_1, score_2 = 0,0
    for point in lines[2:]:
        if team_1 in point:
            score_1 += int(point.strip().replace(team_1, "").replace(" ", ""))
        else: score_2 += int(point.strip().replace(team_2, "").replace(" ", ""))
    return team_1 if score_1 > score_2 else team_2
