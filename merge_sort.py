def merge_result(array, a, b, x, y):
    tmp = [0] * (b - a + 1 + y - x + 1)
    i, j = a, x
    k = 0
    while i <= b and j <= y:
        if array[i] <= array[j]:
            tmp[k] = array[i]
            i += 1
        else:
            tmp[k] = array[j]
            j += 1
        k += 1
    while i <= b:
        tmp[k] = array[i]
        i += 1
        k += 1
    while j <= y:
        tmp[k] = array[j]
        j += 1
        k += 1
    for t in tmp:
        array[a] = t
        a += 1


def merge_sort(array, s, e):
    if s >= e:
        return
    if s == (e - 1):
        if array[s] > array[e]:
            array[s], array[e] = array[e], array[s]
        return
    mid = int((s + e) / 2)
    merge_sort(array, s, mid)
    merge_sort(array, mid + 1, e)
    merge_result(array, s, mid, mid + 1, e)


if __name__ == '__main__':
    s = [1, 3, 2, 4, -1]
    merge_sort(s, 0, len(s) - 1)
    print s
