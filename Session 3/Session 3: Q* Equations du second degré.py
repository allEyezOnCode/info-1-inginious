def rho(a, b, c):
    return b**2 - 4 * a * c
def n_solutions(a, b, c):
    rho_val = rho(a, b, c)
    return 0 if rho_val < 0 else 1 if rho_val == 0 else 2

def solution(a, b, c):
    rho_val = racine_carree(rho(a, b, c))
    first_soluce = (-b - rho_val) / (2*a)
    soluce_2 = (-b + rho_val) / (2*a)
    return min(first_soluce, soluce_2)
