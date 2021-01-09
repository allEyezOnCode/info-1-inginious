def matrix_for_traces(l, theta1, theta2):
    return [[cross(trace, trace2, theta1, theta2) for trace2 in l] for trace in l]

def cross(trace, trace2, theta1, theta2):
    for el in trace:
        for el2 in trace2:
            if abs(el[0] - el2[0]) <= theta1 and abs(euclidian_distance(el[1], el2[1])) < theta2:
                return 1
    return 0
