s, n = map(int, input().split())
gold = [0] + list(map(int, input().split()))

dp = [[0] * (s + 1) for i in range(n+1)]
dp[0][0] = 1

for i in range(1, n + 1):
  wi = gold[i]
  for j in range(s + 1):
    dp[i][j] = dp[i - 1][j]
    if j - wi >= 0 and dp[i - 1][j - wi] == 1:
       dp[i][j] = 1
for j in range(s, -1, -1):
    if dp[n][j] == 1:
        print(j)
        break
