tup = tuple(input().split())
print("The original tuple is : " + str(tup))
result = True
temp = set()
for i in tup:
    if i in temp:
        result = False
        break
    temp.add(i)
print("Is tuple distinct ? : " + str(result))
