def is_palindrome(a, b, s):
    if a > b:
        return True
    if s[a] != s[b]:
        return False
    a += 1
    b -= 1
    return is_palindrome(a, b, s)


def check_palindrome(s):
    length = len(s)
    a = 0
    b = length - 1
    return is_palindrome(a, b, s)


input_s = str(input())
print(check_palindrome(input_s))
