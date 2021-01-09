for i in range(1, n+1):
    count = 0
    for nb in range(2, i+1):
        if not i % nb:
            count += 1
    print(f'{i} : {count}')
