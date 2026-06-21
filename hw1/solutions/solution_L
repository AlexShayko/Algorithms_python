n = int(input())

if n >= 10**6 + 3:
    print(0)
else:
    fact = 1
    for i in range(1, n + 1):
        fact = ((fact) * (i % (10**6 + 3))) % (10**6 + 3)
    print(fact)
