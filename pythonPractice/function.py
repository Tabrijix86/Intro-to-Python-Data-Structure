def myfunction(x, z, y=10):
    print("x =", x, "y =", y, "z =", z)


myfunction(1, 2, 5)
myfunction(x=1, y=2, z=5)
a = 5
b = 6
myfunction(x=a, z=b)
a = 1
b = 2
c = 3
myfunction(y=a, z=b, x=c)
