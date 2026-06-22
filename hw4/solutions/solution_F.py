n, list1, m, list2 = int(input()), list(map(int, input().split())), int(input()), list(map(int, input().split()))
def min_razn(A, B):
    min = abs(A[0] - B[0])
    if min == 0:
        return A[0], B[0]
    mins = [A[0], B[0]]
    i=j=0
    while i < n and j < m:
        if abs(A[i]-B[j]) < min:
            min = abs(A[i]-B[j])
            mins[0] = A[i]
            mins[1] = B[j]
            if min == 0:
                return mins[0], mins[1]
        
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    return mins[0], mins[1]

print(*min_razn(list1, list2))
