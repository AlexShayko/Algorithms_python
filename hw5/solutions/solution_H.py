N = int(input())

if N == 1:
    print(0)
    print(1)
else:
    dp = [float('inf')] * (N + 1)
    parent = [-1] * (N + 1)

    dp[1] = 0

    for i in range(1, N):
        if dp[i] == float('inf'):
            continue

        next_val = i * 2
        if next_val <= N and dp[i] + 1 < dp[next_val]:
            dp[next_val] = dp[i] + 1
            parent[next_val] = i

        next_val = i * 3
        if next_val <= N and dp[i] + 1 < dp[next_val]:
            dp[next_val] = dp[i] + 1
            parent[next_val] = i

        next_val = i + 1
        if next_val <= N and dp[i] + 1 < dp[next_val]:
            dp[next_val] = dp[i] + 1
            parent[next_val] = i

    path = []
    current = N
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()

    print(dp[N])
    print(*path)
