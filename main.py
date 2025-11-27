from Willians import is_prime_wilson
from Trial import is_prime_trial
from miller_rabin import is_prime_mr
from nth_prime import nth_prime

def test(detector, name):
    print(f"\nUsing detector: {name}")
    for k in [1, 2, 3, 10, 100]:
        print(f"  p_{k} = {nth_prime(k, detector)}")

def main():
    test(is_prime_wilson, "wilson")
    test(is_prime_trial, "trial")
    test(is_prime_mr, "miller-rabin")

if __name__ == "__main__":
    main()
