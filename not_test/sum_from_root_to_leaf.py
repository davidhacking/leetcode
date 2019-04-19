# encoding=utf-8

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.val)


class Solution:
	def calc(self, node, cur):
		if node.left == node.right:
			self.res += int(cur + str(node.val), 2)
			return
		if node.left:
			self.calc(node.left, cur + str(node.val))
		if node.right:
			self.calc(node.right, cur + str(node.val))

	def solve(self, data):
		self.res = 0
		self.calc(data, "")
		return self.res


if __name__ == '__main__':
	root = Node(1, Node(0, Node(0), Node(1)), Node(1, Node(0), Node(1)))
	s = Solution()
	print s.solve(root)
