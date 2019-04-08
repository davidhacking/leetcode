# encoding=utf-8
import os, sys


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def traverse_func(node):
    sys.stdout.write(node.val + ", ")


def mid_traverse(node, visit=traverse_func):
    if not node: return
    mid_traverse(node.left)
    visit(node)
    mid_traverse(node.right)


def left_traverse(node, visit=traverse_func):
    if not node: return
    visit(node)
    left_traverse(node.left)
    left_traverse(node.right)


def right_traverse(node, visit=traverse_func):
    if not node: return
    right_traverse(node.left)
    right_traverse(node.right)
    visit(node)


def mid_stack_traverse(node, visit=traverse_func):
    stack = []
    cur = node
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            visit(cur)
            cur = cur.right


def left_stack_traverse(node, visit=traverse_func):
    stack = []
    cur = node
    while stack or cur:
        if cur:
            visit(cur)
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            cur = cur.right


def right_stack_traverse2(node, visit=traverse_func):
    cur = node
    stack = []
    visit_stack = []
    while cur or stack:
        if cur:
            visit_stack.append(cur)
            stack.append(cur)
            cur = cur.right
        else:
            cur = stack.pop()
            cur = cur.left
    while visit_stack:
        visit(visit_stack.pop())


def right_stack_traverse(node, visit=traverse_func):
    cur = node
    pre = None
    stack = []
    while cur or stack:
        if cur:
            if cur.right is None and cur.left is None:
                visit(cur); pre = cur; cur = None
            elif ((cur.right and cur.left is None) or (cur.right is None and cur.left))\
                    and ():
                if cur.right and cur.right == pre:
                    visit(cur); pre = cur; cur = None
                elif cur.left and cur.left == pre:
                    visit(cur); pre = cur; cur = None
            else:
                if cur.right:
                    stack.append(cur.right)


if __name__ == '__main__':
    root = Node('A', Node('B', Node('D'), Node('E')), Node('C', Node('F'), Node('G')))
    print "mid"
    mid_traverse(root)
    print ""
    mid_stack_traverse(root)
    print ""

    print "left"
    left_traverse(root)
    print ""

    left_stack_traverse(root)
    print ""

    print "right"
    right_traverse(root)
    print ""

    right_stack_map_traverse(root)
    print ""
    # right_stack_traverse_like_stack(root)
    # print ""
