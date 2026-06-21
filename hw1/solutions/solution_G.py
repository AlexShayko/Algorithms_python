sum = 0
s = [0]*(int(input()) + 1)
for i in range(2, len(s)):
    if s[i] == 0:
        sum += i
        for j in range(i + i, len(s), i):
            if s[j] == 0:
                s[j] = 1
                sum += i
print(sum)


