def is_prime_wilson(x: int) -> bool:
    if x < 2:
        return False
    # Wilson: (x-1)! % x == x-1
    fact = 1
    for i in range(1, x):
        fact = (fact * i) % x
    return fact == x - 1