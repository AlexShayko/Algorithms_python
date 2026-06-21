n, k = map(int, input().split())
nums = [str(x) for x in range(k)]
def gena(head,tail):
  if len(tail) == n:
    print(tail)
  else:
    for i in range(len(head)):
      gena(head, tail + head[i])

gena(nums, '')
