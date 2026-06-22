n = int(input())
list0 = list(map(int, input().split()))

def merge(A, B):
    i=j=0
    result = [0] * (len(A) + len(B))
    while i != len(A) or j != len(B):
        if i == len(A):
            result[i+j] += B[j]
            j += 1
        elif j == len(B):
            result[i+j] += A[i]
            i += 1
        elif A[i] < B[j]:
            result[i + j] += A[i]
            i +=1
        else:
            result[i + j] += B[j]
            j += 1
    return result

def MergeSort(A):
    if len(A) < 2:
        return A
    else:
        mid = len(A)//2
    return(merge(MergeSort(A[:mid]), MergeSort(A[mid:])))

print(*MergeSort(list0))
