n = int(input())
dp=[0]*(n+1)
dp[0] = 0
dp[1] = 3
if n == 2:
	dp[2] = 8
elif n > 2:
    dp[2]= 8
    for i in range(3, n+1):
        dp[i] = 2*dp[i-1]+2*dp[i-2]
print(dp[-1])
