n, a1, k, b, m = map(int, input().split())

a = [0] * n
a[0] = a1
for i in range(1, n):
    a[i] = (k * a[i - 1] + b) % m

d = []

def bin_search(arr, x):
    left = 0
    right = len(arr) - 1
    pos = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= x:
            pos = mid
            right = mid - 1
        else:
            left = mid + 1
    return pos

for x in a:
    pos = bin_search(d, x)
    if pos == len(d):
        d.append(x)
    else:
        d[pos] = x

print(len(d))

