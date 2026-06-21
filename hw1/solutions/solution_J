n = int(input())
if n == 0 or n == 1:
    print(1)
else:
    f = [0] * (n + 1)
    f[0], f[1] = 1, 1
    for i in range(2, n + 1):
        f[i] = (f[i - 1] % (10**6 + 3) + f[i - 2] % (10**6 + 3)) % (10**6 + 3)
    print(f[n])
