list_nums = list(map(int, input().split()))
def SelectionSort(A):
    for i in range(len(A) - 1):
        max_el_ind = i
        for j in range(i + 1, len(A)):
            if A[j] > A[max_el_ind]:
                max_el_ind = j
        if max_el_ind != i:
            A[i], A[max_el_ind] = A[max_el_ind], A[i]
    return A
print(*SelectionSort(list_nums))
