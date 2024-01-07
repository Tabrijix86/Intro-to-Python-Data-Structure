L = [str(x) for x in range(100)]
print(L)

s = ""
for x in L:
    s += " " + x  # Avoid doing this, it creates a new string at every iteration
print(s)  # Note the redundant initial space
print(" ".join(L))  # This is the correct way of building a string out of smaller strings
print('abc--def--ghi'.split(sep="--"))
# If no parameters are given to the split method, then it splits at any sequence of white space.
