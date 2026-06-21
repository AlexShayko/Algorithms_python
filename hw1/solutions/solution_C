x, y = int(input()), int(input())

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b
print(int((x*y)/gcd(x, y)))
