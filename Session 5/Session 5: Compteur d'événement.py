def count(events, i, j):
    return sum(1 for event in events if event == (i, j))
