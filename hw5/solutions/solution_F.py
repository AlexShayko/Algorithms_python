n = int(input())
if n == 0:
    print(0)
else:
    prices = [0] + list(map(int, input().split()))
    if n == 1:
        print(prices[1])
    else:
        dp = [0] * (n + 1)
        dp[1] = prices[1]
        for i in range(2, n + 1):
            dp[i] = prices[i] + min(dp[i-1], dp[i-2])

        print(dp[n])
