def find_left(a, x):
    l = 0
    r = len(a)
    while l < r:
        m = (l + r) // 2
        if a[m] < x:
            l = m + 1
        else:
            r = m
    return l

def lis_len(arr):
    tails = []
    for num in arr:
        p = find_left(tails, num)
        if p == len(tails):
            tails.append(num)
        else:
            tails[p] = num
    return len(tails)

def min_pops(arr):
    n = len(arr)
    if n <= 1:
        return 0
    max_lis = lis_len(arr)
    return n - max_lis

n = int(input())
a = list(map(int, input().split()))

print(min_pops(a))
