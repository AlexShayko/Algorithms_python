A, K, B, M, X = map(int, input().split())

def trees_cut(t):
    return A * (t - t//K) + B * (t - t//M)

l = 0
r = 1
while trees_cut(r) < X:
    r *=2

while l < r:
    mid = (l + r) // 2
    if trees_cut(mid) >= X:
        r = mid
    else:
        l = mid + 1

print(l)
