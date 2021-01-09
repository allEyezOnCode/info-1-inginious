fact = lambda x: 1 if x <= 1 else x * fact(x-1)
result = fact(x)
