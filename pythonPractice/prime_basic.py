def is_prime(n):
    if n < 2:
        return False
    prime = True
    for i in range(2, n):
        if n % i == 0:
            print(n, "is divisible by", i)
            prime = False

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
