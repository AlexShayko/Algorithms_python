n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

def bin_search(n, k):
    if sum(arr) < k:
        return 0

    l = 1
    r = max(arr)
    ans = 0

    while l <= r:
        mid = (l + r) // 2
        total = 0
        for i in range(n):
            total += arr[i] // mid
        if total >= k:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    return ans

print(bin_search(n, k))
