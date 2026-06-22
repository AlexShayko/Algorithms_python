def bin_pow(a, n, p):
  if n == 0:
    return 1
  if n % 2:
    return bin_pow(a, n-1, p) * a % p 
  return bin_pow((a * a) % p, n // 2, p) 
T = int(input())
p = 10**9 + 9
for _ in range(T):
    a = int(input())
    print(bin_pow(a, p - 2, p))
	
