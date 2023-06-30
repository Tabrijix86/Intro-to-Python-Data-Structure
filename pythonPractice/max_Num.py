n1 = input("Please enter first number: ")
n2 = input("Please enter second number: ")
n3 = input("Please enter third number: ")

if n1 > n2:
    max_n = n1
else:
    max_n = n2
if n3 > max_n:
    max_n = n3

print("Maximum: ", max_n)
