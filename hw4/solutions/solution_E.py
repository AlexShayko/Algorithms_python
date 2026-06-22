n = int(input())
list0 = list(map(int, input().split()))
def DigitSort(A):
    max_num = max(A)
    num_digits = len(str(max_num))
    for i in range(0, num_digits):
        list_for_step = [[] for j in range(10)]
        for el in A:
            list_for_step[(el//10**i)%10].append(el)
        A = []
        for dig in list_for_step:
            A.extend(dig)
    return A
print(*DigitSort(list0))
