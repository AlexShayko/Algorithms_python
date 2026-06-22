w, h, n = map(int, input().split())

def min_side(w, h, n):
    l = 0
    r = max(w, h) * n
    while l + 1 < r:
        mid = (l + r) // 2
        if (mid // w) * (mid // h) >= n:
            r = mid
        else:
            l = mid
    return r

print(min_side(w, h, n))
