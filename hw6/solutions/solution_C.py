n, k = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

def bin_search(el, arr):
    l = -1
    r = len(arr)
    while l + 1 < r:
        mid = (l + r) // 2
        if arr[mid] == el:
            return 'YES'
        elif arr[mid] < el:
            l = mid
        else:
            r = mid
    return 'NO'


for el in list2:
    print(bin_search(el, list1))
