n = int(input())
dp = [[1] * (n + 1) for i in range(n + 1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
dp_new = [[0] * n for i in range(n)]

for r in range(n):
    row = []
    for k in range(r + 1): 
        row.append(str(dp[k][r - k]))
    print(' '.join(row))
