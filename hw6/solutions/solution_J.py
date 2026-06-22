n, a, b, w, h = map(int, input().split())

def can_place(d):

    A = a + 2 * d
    B = b + 2 * d

    cnt1 = (w // A) * (h // B)

    cnt2 = (w // B) * (h // A)

    return cnt1 >= n or cnt2 >= n

def bin_search(left, right):

    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if can_place(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer


max_d = 10**18

result = bin_search(0, max_d)
print(result)
