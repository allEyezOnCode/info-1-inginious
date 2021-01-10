def fibonacci(n):
    if n <= 0:
        return 0
    first = second = 1
    for i in range(2, n):
        first, second = second, first + second
    return second

# Recursive approach inefficient
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     if n <= 2:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)
