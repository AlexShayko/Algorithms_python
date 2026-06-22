def gcd_extended(a, b):
    if b == 0:
        return (1, 0, a)
    x1, y1, d = gcd_extended(b, a % b)
    return (y1, x1 - (a // b) * y1, d)

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    
    x0, y0, d = gcd_extended(a, b)
    
    if c % d != 0:
        print("0 0")
    else:
        k = c // d
        x0 *= k
        y0 *= k

        step = b // d
        x_min = x0 % step
        if x_min < 0:
            x_min += step

        t_val = (x_min - x0) // step
        y_min = y0 - (a // d) * t_val
        
        print(x_min, y_min)
