n, k = map(int, input().split())

def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

n = n // gcd(n,k)
print(n * k)
