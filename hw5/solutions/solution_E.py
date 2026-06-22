n, k = map(int, input().split())
l = int(input())
frogs = list()
if l != 0:
    frogs = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    if i in frogs:
        continue
    s = 0
    for j in range(1, k + 1):
        if i - j >= 1:
            s += dp[i - j]
    dp[i] = s

print(dp[n])
