n, s = map(int, input().split())
weights = [0] + list(map(int, input().split()))
prices = [0] + list(map(int, input().split()))

dp = [[0] * (s + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, s + 1):
        dp[i][j] = dp[i - 1][j]
        if j - weights[i] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - weights[i]] + prices[i])
x = s
selected_items = []
for i in range(n, 0, -1):
    if dp[i][x] != dp[i - 1][x]:
        selected_items.append(i)
        x -= weights[i]
selected_items.reverse()

for item in selected_items:
    print(item, end=' ')
