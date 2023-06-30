# Function to find HCF the Using Euclidian algorithm
def compute_hcf(x, y):
    while y:
        x, y = y, x % y
    return x


hcf = compute_hcf(300, 400)
print("The HCF is", hcf)


def gcd(x, y):
    if x == 0:
        return y
    return gcd(y % x, x)
