list_prost_nums = []
n = int(input())
places = [int(x) for x in input().split()]
s = [0] * (1299709 + 1)
for i in range(2, len(s)):
    if s[i] == 0:
        list_prost_nums.append(i)
        for j in range(i + i, len(s), i):
            s[j] = 1
for i in range(n):
    print(list_prost_nums[places[i] - 1], end=' ')


