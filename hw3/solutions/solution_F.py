a, n = float(input()), int(input())
def bin_pow(a, n):
    if n < 0:
        n = n * (-1)
    if n == 0:
        return 1
    if n % 2:
        return bin_pow(a, n-1) * a
    half = bin_pow(a, n//2)
    return half * half

if n >= 0:
    print(bin_pow(a, n))
else:
    print(1/bin_pow(a, n))
