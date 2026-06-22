a, b, c, d = map(int, input().split())

def f(x):
    return a*(x**3) + b*(x**2) + c*x + d

left = -1000000000000
right = 1000000000000
eps = 1e-12

while right - left > eps:
    mid = (left + right) / 2
    if f(mid)*f(left) <= 0:
        right = mid
    else:
        left = mid

root = (left + right) / 2
print(root)

