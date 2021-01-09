sum_even = 0
x = 0
it = iter(matrix)
try:
    while True:
        it2 = iter(next(it))
        try:
            while True:
                val = next(it2)
                if val % 2 == 0:
                    sum_even += val
        except: pass
except Exception as error: print(error)
