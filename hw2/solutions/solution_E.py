n, k = map(int, input().split())
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
if k < 10:
    nums = [str(k-1-x) for x in range(k)]
else:
    nums = [char for char in alphabet[: k-10][::-1]]
    nums += [str(9 - x) for x in range(10)]

def gena(head,tail):
    if len(tail) == n:
        print(tail)
    else:
        for i in range(len(head)):
            gena(head, tail + head[i])

gena(nums, '')
