mod = 10**9 + 7
a, b, c, d = map(int, input().split())

a %= mod
b %= mod
c %= mod
d %= mod

numerator = (a * d + b * c) % mod
denominator = (b * d) % mod

def bin_pow(a, n, p):
    if n == 0:
        return 1
    if n % 2:
        return bin_pow(a, n-1, p) * a % p 
    return bin_pow((a * a) % p, n // 2, p) 

inv_denom = bin_pow(denominator, mod - 2, mod)
result = (numerator * inv_denom) % mod
print(result)
