def primes(max_):
    prime_lst = []
    for n in range(2, max_+1):
        if next((False for el in prime_lst if not n % el), True):
            prime_lst.append(n)
    return prime_lst
