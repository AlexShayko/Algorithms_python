n = int(input())
k = int(input())

def C(n, k):
    if k == 0 or k == n:
        return 1
    return C(n-1, k-1) + C(n-1, k)

print(C(n, k))
