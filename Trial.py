import math

def is_prime_trial(x: int) -> bool:
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    r = int(math.sqrt(x))
    for i in range(3, r + 1, 2):
        if x % i == 0:
            return False
    return True
