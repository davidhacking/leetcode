# encoding=utf-8


class ArrayStack(object):
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def push(self, val):
        self.stack.append(val)

    def is_empty(self):
        return self.stack.__len__() == 0

    def __str__(self):
        return str(self.stack)


if __name__ == "__main__":
    stack = ArrayStack()
    print stack.is_empty()
    stack.push(1)
    stack.push(2)
    print stack
    print stack.pop()
    print stack
    print stack.top()
    pass
