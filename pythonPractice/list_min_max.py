li = [1, 1, 2, 2, 3, 4, 5]
minimum = min(li)
print(minimum)
li.remove(minimum)
print(li)
new_minimum = min(li)
li.remove(new_minimum)
print(li)
