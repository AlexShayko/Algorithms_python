n, l = map(int, input().split())
times = list(map(int, input().split()))
final_times = []
for i in range(1, len(times) + 1):
    final_times.append( i - 1 + l * times[i-1] )

cnt = 0


def merge(a: list[int], b: list[int]) -> list[int]:
    global cnt
    c = [0] * (len(a) + len(b))
    i = j = 0
    while i < len(a) or j < len(b):
        if i == len(a):
            c[i + j] = b[j]
            j += 1
        elif j == len(b):
            c[i + j] = a[i]
            i += 1
        elif a[i] > b[j]:
            c[i + j] = b[j]
            cnt += len(a) - i
            j += 1
        else:
            c[i + j] = a[i]
            i += 1

    return c


def merge_sort(a: list[int]) -> list[int]:
    if len(a) < 2:
        return a
    mid = len(a) // 2
    return merge(merge_sort(a[:mid]), merge_sort(a[mid:]))

merge_sort(final_times)
print(cnt)
