def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            while n % divisor == 0:
                n //= divisor
        divisor += 1

    factors.reverse()
    return factors

def print_prime_factors(n):
    factors = prime_factors(n)
    for factor in factors:
        print(factor)

if __name__ == "__main__":
    number = 8
    print_prime_factors(number)
