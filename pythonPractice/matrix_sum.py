m = int(input("Enter number of rows for matrix A: "))
n = int(input("Enter number of columns for matrix A: "))

matrixA = []
for i in range(m):
    rowA = []
    for j in range(n):
        element = int(input(f"Enter element: [{i + 1, j + 1}]: "))
        rowA.append(element)
    matrixA.append(rowA)

o = int(input("Enter number of rows for matrix B: "))
p = int(input("Enter number of columns for matrix B: "))
matrixB = []
for i in range(o):
    rowB = []
    for j in range(p):
        element = int(input(f"Enter element: [{i + 1, j + 1}]: "))
        rowB.append(element)
    matrixB.append(rowB)
matrixS = []
for i in range(o):
    rowS = []
    for j in range(p):
        element = 0
        rowS.append(element)
    matrixS.append(rowS)
for i in range(len(matrixA)):
    for j in range(len(matrixA[0])):
        matrixS[i][j] = matrixA[i][j] + matrixB[i][j]

print("Sum of matrix A and B is: ", end="\n")
for s in matrixS:
    print(s)
