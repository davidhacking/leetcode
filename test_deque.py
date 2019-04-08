

if __name__ == '__main__':
    from collections import deque
    d = deque('ddddddd')
    d.append('1')
    d.appendleft('22')
    d.rotate(1) # pop and appendleft
    print d
    print d.pop()
    print d.popleft()
    d.reverse()
    print d