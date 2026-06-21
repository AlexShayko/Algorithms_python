n, k = map(int, input().split())
def gena(tail):
  if len(tail) == n:
    print(*tail)
  else:
    for i in range(1, k + 1):
      gena(tail + [i])

gena([])
