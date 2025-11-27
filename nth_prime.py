from Bounds  import upper_bound_for_prime

def nth_prime(n: int, detector) -> int:
    bound = upper_bound_for_prime(n)
    count = 0

    for x in range(2, bound + 1):
        if detector(x):
            count += 1
            if count == n:
                return x

    raise Exception("Upper bound failed — should not happen")
