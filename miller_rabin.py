def is_prime_mr(n: int) -> bool:
    if n < 2:
        return False

    # small primes
    small_primes = [2, 3, 5, 7, 11, 13, 17]
    if n in small_primes:
        return True
    for p in small_primes:
        if n % p == 0:
            return False

    # write n-1 = 2^r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        r += 1
        d //= 2

    # Deterministic bases for 64-bit
    bases = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]

    def check(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False

    return all(check(a) for a in bases if a < n)
