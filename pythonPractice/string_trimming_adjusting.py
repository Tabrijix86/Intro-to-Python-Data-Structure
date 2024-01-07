L = [1, 3, 5, 7, 9, 1, 1]
print("-" * 52)
for i in L:
    s = "*" * i
    print(f"|{s.center(50)}|")
print("-" * 52)

# s.strip(x) Removes leading and trailing whitespace by default, or characters found in string x
# s.lstrip(x) Same as strip but only leading characters are removed
# s.rstrip(x) Same as strip but only trailing characters are removed
# s.ljust(n) Left justifies string inside a field of length n
# s.rjust(n) Right justifies string inside a field of length n
# s.center(n) Centers string inside a field of length n
