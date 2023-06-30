import math


def is_prime(n):
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


while True:
    number = int(input("Please enter a number (Enter 0 to exit): "))
    if number == 0:
        break
    prime_num = is_prime(number)
    if prime_num is True:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")
