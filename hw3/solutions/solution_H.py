def hanoi_piram(disk_quant, first, last, middle):
    if disk_quant == 1:
        print(f"1 {first} {last}")
    else:
        hanoi_piram(disk_quant - 1, first, middle, last)
        print(f"{disk_quant} {first} {last}")
        hanoi_piram(disk_quant - 1, middle, last, first)

n = int(input())
hanoi_piram(n, 1, 3, 2)
