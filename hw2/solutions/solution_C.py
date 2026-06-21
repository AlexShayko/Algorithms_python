n = int(input())
def gena(head,tail):
  if len(tail) == n:
    print(tail)
  else:
    for i in range(len(head)):
      gena(head, tail + head[i])

gena('10', '')
