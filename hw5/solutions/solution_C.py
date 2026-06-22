n = int(input())
def count_str(symb_quant):
    if symb_quant == 0:
        return 0
    elif symb_quant == 1:
        return 2
    elif symb_quant == 2:
        return 3
    else:
        return count_str(symb_quant-1) + count_str(symb_quant-2)
print(count_str(n))
