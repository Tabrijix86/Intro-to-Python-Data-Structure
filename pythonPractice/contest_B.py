n = int(input())
for i in range(n):
    li = str(input())
    if len(li) >= 10:
        print(li[0]+str((len(li) - 2)) + li[-1])
    else:
        print(li)
