# copying the elements
aList = [1, 2, 3]
bList = aList[:]
aList[0] = 123
print(aList)
print(bList)
print("Compare the reference of aList and bList")
print("id(aList):", id(aList))
print(f"id(bList): {id(bList)}")

#  copying the reference to the list
aList = [1, 2, 3]
bList = aList
aList[0] = 123
print(bList)

print("Compare the reference of aList and bList")
print(f"id(aList): {id(aList)}")
print(f"id(bList): {id(bList)}")
