n, k = map(int, input().split())

def gruz_count(quant, volume):
    if quant <= volume:
        return 1
    else:
        if quant % 2 == 0:
            return 2 * gruz_count(quant//2, volume)
        else:
            return gruz_count(quant//2, volume) + gruz_count(quant//2 + 1, volume)
print(gruz_count(n, k))




