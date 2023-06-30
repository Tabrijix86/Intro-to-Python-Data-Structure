import math
import timeit


def is_prime4(n=11):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = int(math.sqrt(n)) + 1
    for i in range(3, m, 2):
        if n % i == 0:
            return False
    return True


def is_prime3(n=11):
    if n == 2:
        return True  # 2 is prime
    if n % 2 == 0:
        return False  # all even numbers except 2 are not prime
    if n < 2:
        return False  # numbers less than 2 are not prime
    prime = True
    m = (n // 2) + 1
    for i in range(3, m, 2):
        if n % i == 0:
            prime = False
            return prime
    return prime


run_time_4 = timeit.timeit(is_prime4)
run_time_3 = timeit.timeit(is_prime3)

print("\nSquare root method:", run_time_4, "VS Division method:", run_time_3, "\n")
