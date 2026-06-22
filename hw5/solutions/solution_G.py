n = int(input())
values = list(map(int, input().split()))
s = int(input())

if s == 0:
    print(0)
    print()
else:
    values = sorted([v for v in values if v <= s])

    INF = 10**9
    dp = [INF] * (s + 1)
    parent = [-1] * (s + 1)
    dp[0] = 0

    for i in range(1, s + 1):
        for val in values:
            if val > i:
                break
            if dp[i - val] + 1 < dp[i]:
                dp[i] = dp[i - val] + 1
                parent[i] = val

    if dp[s] == INF:
        print(-1)
    else:
        print(dp[s])
        result = []
        curr = s
        while curr > 0:
            coin = parent[curr]
            result.append(coin)
            curr -= coin
        print(*result)
