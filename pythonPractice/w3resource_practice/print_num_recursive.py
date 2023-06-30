def print_num(n):
    if n <= 50:
        print(n, end=" ")
    else:
        return
    return print_num(n + 1)


print_num(1)
