n, p = map(int, input().split())
moods = list(map(int, input().split()))

ext_moods = moods * 2

min_len = n + 1
best_start = -1
right = 0
cur_sum = 0

for left in range(n):
    while right < left + n and right < 2 * n and cur_sum < p:
        cur_sum += ext_moods[right]
        right += 1

    if cur_sum >= p:
        curr_len = right - left
        if curr_len < min_len or (curr_len == min_len and (best_start == -1 or left + 1 < best_start)):
            min_len = curr_len
            best_start = left + 1

    if right > left:
        cur_sum -= ext_moods[left]

if min_len == n + 1:
    print(-1)
else:
    print(best_start, min_len)
