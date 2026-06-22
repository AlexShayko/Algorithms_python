n = int(input())
if n == 0:
    print(1)
elif n == 1:
    print(1)
else:
    dp=[0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, len(dp)):
        if i % 2 == 0:
            dp[i] = dp[i//2] + dp[i//2 - 1]
        else:
            dp[i] = dp[i//2] - dp[i//2 - 1]
    print(dp[n])
