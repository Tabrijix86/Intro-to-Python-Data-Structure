# def LCM(a, b):
#
#     if a > b:
#         greater = b
#     else:
#         greater = a
#     for i in range(greater, (a * b)+1):
#         if (i % a == 0) and (i % b == 0):
#             lcm = i
#             break
#
#     return lcm
#
#
# num1 = int(input("Enter the first integer: "))
# num2 = int(input("Enter the second integer: "))
# print(f"The Least Common Multiple of {num1} and {num2} is {LCM(num1, num2)}")
# # # Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):
    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm


num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))
