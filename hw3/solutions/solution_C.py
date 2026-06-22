n = int(input())
def phib_count(num):
    if num == 1 or num == 2:
        return 1
    else:
        return 1 + (phib_count(num - 1) + phib_count(num - 2))

print(phib_count(n))
