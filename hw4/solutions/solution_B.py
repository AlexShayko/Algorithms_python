n = int(input())
list_nums = list(map(int, input().split()))
def CountSort(A):
    min_A = min(A)
    max_A = max(A)
    count_list = [0]*(max_A - min_A + 1)
    for i in range(len(A)):
        count_list[A[i] - min_A] += 1
    for i in range(len(count_list)):
        for _ in range(count_list[i]):
            print(i + min_A, end=' ')
CountSort(list_nums)
