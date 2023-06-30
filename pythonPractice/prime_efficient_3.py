def is_prime(n):
    if n == 2:
        return True  # 2 is prime
    if n % 2 == 0:
        print(n, "is divisible by 2")
        return False  # all even numbers except 2 are not prime
    if n < 2:
        return False  # numbers less than 2 are not prime
    prime = True
    m = (n // 2) + 1
    for i in range(3, m, 2):
        if n % i == 0:
            print(n, "is divisible by", i)
            prime = False
            return prime
    return prime


while True:
    number = int(input("Please enter a number (Enter 0 to exit): "))
    if number == 0:
        break
    prime_num = is_prime(number)
    if prime_num is True:
        print(number, "is a prime number.")
    else:
        print("So,", number, "is not a prime number.")
