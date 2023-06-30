def total_sum(n):
    if n == 1:
        return 1
    else:
        total = n + total_sum(n - 1)
    return total


limit = int(input())
print(total_sum(limit))
