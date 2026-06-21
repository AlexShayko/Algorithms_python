x1, y1, x2, y2 = map(int, input().split())

dx = x2 - x1
dy = y2 - y1

def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

print(gcd(dx, dy) + 1)
