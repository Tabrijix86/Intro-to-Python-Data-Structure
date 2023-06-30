def fibonacci(n):
    if n <= 1:
        return 1  # use n in order to print 0 first
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input())
if num <= 0:
    print("Please enter a positive number!")
else:
    for i in range(num):
        print(fibonacci(i), end=" ")
