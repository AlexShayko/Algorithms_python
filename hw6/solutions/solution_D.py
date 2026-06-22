n = int(input())
array = sorted(list(map(int, input().split())))
k = int(input())

def bin_first(arr, k):
    l, r = -1, len(arr)
    while l + 1 < r:
        m = (l + r) // 2
        if arr[m] < k:
            l = m
        else:
            r = m
    return r

def bin_last(arr, k):
    l, r = -1, len(arr)
    while l + 1 < r:
        m = (l + r) // 2
        if arr[m] <= k:
            l = m
        else:
            r = m
    return l



for _ in range(k):
    l, r = map(int, input().split())
    print((bin_last(array, r) - bin_first(array, l) + 1), end=' ')
