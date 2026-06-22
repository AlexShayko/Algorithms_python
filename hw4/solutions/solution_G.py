n = int(input())
letters = input()
quant = [0] * 26

for lt in letters:
    index = ord(lt) - ord('A')
    quant[index] += 1

pairs = []
for count in quant:
    pairs.append(count // 2)

remains = []
for count in quant:
    remains.append(count % 2)

central=''
if any(remains):
    for i in range(26):
        if remains[i] != 0:
            central = chr(i + ord('A'))
            break

polinom=''

if any(pairs):
    for i in range(26):
        polinom += chr(i + ord('A'))*pairs[i]

polinom += central
if central:
    polinom_half = polinom[:len(polinom) - 1][::-1]
else:
    polinom_half = polinom[::-1]

print(polinom + polinom_half)
