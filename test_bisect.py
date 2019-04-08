# encoding=utf-8

if __name__ == '__main__':
    import bisect
    a = [1, 2, 3, 4, 5,]
    print bisect.bisect_left(a, 5) #4 a[i:] have e >= x
    print bisect.bisect_right(a, 5) #5 a[i:] have e > x
    print bisect.bisect_left(a, 0) #0
    print bisect.bisect_right(a, 0) #0
    print bisect.bisect_left(a, 10) #5
    bisect.insort_left(a, 10)
    bisect.insort_left(a, 5)
    print a