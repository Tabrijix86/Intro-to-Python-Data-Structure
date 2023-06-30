name = str(input()).split()
print("Given name: ", end="")
for i in range(0, len(name) - 1):
    print(name[i], end=" ")
print(f"\nSurname: {name[-1]}")
