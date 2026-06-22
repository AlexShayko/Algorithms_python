def bin_search(n, k, stoyla):
    left = 0
    right = stoyla[-1] - stoyla[0]
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        cows_placed = 1
        last_pos = stoyla[0]

        for i in range(1, n):
            if stoyla[i] - last_pos >= mid:
                cows_placed += 1
                last_pos = stoyla[i]

        if cows_placed >= k:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

n, k = map(int, input().split())
stoyla = list(map(int, input().split()))
print(bin_search(n, k, stoyla))
