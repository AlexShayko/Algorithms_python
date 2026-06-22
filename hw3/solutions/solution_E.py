a, n = float(input()), int(input())
def bin_pow(a, n):
  if n == 0:
    return 1
  if n % 2:
    return bin_pow(a, n-1) * a
  half = bin_pow(a, n//2)
  return half * half


print(bin_pow(a, n))
