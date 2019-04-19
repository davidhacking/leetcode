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


"""
三种思路
一种就是复用之前的方法，前序遍历是 中左右 后序是 左右中 那只要按照 中右左的方式遍历，这样在最后翻转一次就行了
第二种记录当前节点的右节点有没有进过栈，一种就用map，另一种就在node动态绑定一个属性
第三种判断当前的节点是什么节点，
	如果是叶子节点可以直接访问当前节点，如果是单孩子节点则保证孩子节点已经被访问过了，
		双节点只要之前被访问的是右节点就行，而如果有右节点，那被访问的前一个节点一定是右孩子
		访问之后出栈，记录当前节点是被访问的前一个节点
	如果是双孩子节点则按右左的顺序入栈，出栈的时候就是左右了
	其实思路和第一种有类似的地方，即：按照出栈顺序要是左右中的逆序入栈，而判断条件
"""


def right_stack_traverse1(node, visit=traverse_func):
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


def right_stack_traverse3(node, visit=traverse_func):
	if not node:
		return
	cur = None
	pre = None
	stack = [node]
	while stack:
		cur = stack[-1]
		if cur.left == cur.right or (pre is not None and (cur.left == pre or cur.right == pre)):  # 用来判断是不是都是none
			visit(cur)
			stack.pop()
			pre = cur
		else:
			if cur.right is not None:
				stack.append(cur.right)
			if cur.left is not None:
				stack.append(cur.left)


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

	right_stack_traverse1(root)
	print ""
	right_stack_traverse3(root)
	print ""
