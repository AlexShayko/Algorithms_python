def count_nums_before_bound(n):
    s = int(n**(1/2))
    while (s + 1) ** 2 <= n:
        s += 1
    while s ** 2 > n:
        s -= 1
        
    c = int(n ** (1/3))
    while (c+1)**3 <= n:
        c += 1
    while c**3 > n:
        c -= 1
        
    h = int(n ** (1/6))
    while (h+1)**6 <= n:
        h += 1
    while h**6 > n:
        h -= 1
        
    return s + c - h

def find_Cx(x):
    low, high = 1, 10**18
    while low < high:
        mid = (low + high) // 2
        if count_nums_before_bound(mid) >= x:
            high = mid
        else:
            low = mid + 1
    return low

x = int(input())
print(find_Cx(x))
