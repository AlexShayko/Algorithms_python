def bin_search(x):
    l = -1
    r = 2**32
    while l + 1 < r:
        mid = (l+r)//2
        if mid*mid <= x:
            l = mid
        else:
            r = mid
    return l

while True:
    try:
        x = int(input())
        print(bin_search(x))
    except EOFError:
        break
