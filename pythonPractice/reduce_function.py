from functools import reduce  # import the reduce function from the functools module

L = [1, 2, 3, 4]

print(reduce(lambda x, y: x + y, L, 0))
