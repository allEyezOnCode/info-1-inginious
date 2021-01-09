greatest = None
for n in range(1, a//2+1):
    if not a % n:
        greatest = n
return greatest
