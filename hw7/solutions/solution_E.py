n, m = map(int, input().split())
dp = [[0] * 10 for i in range(8)]
dp[m-1][n] = 1
for i in range(m, 8):
    for j in range(1, 9):
        dp[i][j] = dp[i - 1][j-1] + dp[i-1][j + 1]
print(sum(dp[7]))
