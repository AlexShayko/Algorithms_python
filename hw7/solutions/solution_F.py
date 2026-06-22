n = int(input())
w = list(map(int, input().split()))
ans = sum(w)
for i in range(2**(n-1), 2**n):
    s0 = s1 = 0
    mask = bin(i)[2:]
    for j in range(n):
        if mask[j] == '0':
            s0+=w[j]
        else:
            s1+=w[j]
    ans = min(ans, abs(s0-s1))
print(ans)
