def foo():
  x = int(input())
  if x!=0:
    foo()
  print(x)
foo()
