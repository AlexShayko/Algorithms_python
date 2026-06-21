s = [0]*(int(input()) + 1)
for i in range(2, len(s)):
    if s[i] == 0:
        for j in range(i + i, len(s), i):
            s[j] += 1
for i, v in enumerate(s, 0):
    if v > 2:
        print(i, end=' ')
