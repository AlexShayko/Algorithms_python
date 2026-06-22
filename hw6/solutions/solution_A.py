n = int(input())
if n == 1:
    print(0)
else:
    power = 0
    quest = 1
    while quest < n:
        power += 1
        quest *= 2
    print(power)
