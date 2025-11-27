import math

def upper_bound_for_prime(n: int) -> int:
    if n < 6:
        small = [0, 2, 3, 5, 7, 11]
        return small[n]

    return int(n * (math.log(n) + math.log(math.log(n))))
