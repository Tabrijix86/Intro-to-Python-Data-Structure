def count_dig(n):
    if n == 0:
        return 0
    elif abs(n) // 10 == 0:
        return 1
    else:
        return 1 + count_dig(n // 10)


num = int(input())
print(count_dig(num))
