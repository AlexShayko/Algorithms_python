n = int(input())
w = list(map(int, input().split()))

ans = sum(w)
if ans % 2 != 0:
    print("NO")
else:
    target = ans // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for weight in w:
        for s in range(target, weight - 1, -1):
            if dp[s - weight]:
                dp[s] = True

    print("YES" if dp[target] else "NO")
