n, x, y = map(int, input().split())

def bin_search(n, x, y):
    l = 0
    r = n * max(x, y)
    while l + 1 < r:
        mid = (l + r)//2
        if mid//x + mid//y >= n-1:
            r = mid
        else:
            l = mid
    return r
if n == 1:
    print(min(x, y))
else:
    print(bin_search(n, x, y) + min(x, y))
