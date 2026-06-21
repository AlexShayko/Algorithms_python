n = int(input())
nums = [x + 1 for x in range(n)]
quantity = len(nums)
full_tail = []


def gena(head, tail, cur_sum=0):
    if cur_sum == n:
        full_tail.append(tail)
    elif cur_sum < n:
        if tail:
            last_in_sum = tail[-1]
            start = head.index(last_in_sum)
        else:
            start = 0

        for i in range(start, len(head)):
            gena(head, tail + [head[i]], cur_sum + head[i])
    else:
        return

gena(nums, [])
for x in full_tail[::-1]:
    print(*x)
