# encoding=utf-8

# Definition for a binary tree node.
class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.val)


import math


class Solution(object):
	def dfs(self, node, max_val, min_val):
		if not node:
			return
		max_val = max(max_val, node.val)
		min_val = min(min_val, node.val)
		self.res = max(self.res, max(math.fabs(node.val - max_val), math.fabs(node.val - min_val)))
		if node.left:
			self.dfs(node.left, max_val, min_val)
		if node.right:
			self.dfs(node.right, max_val, min_val)

	def maxAncestorDiff(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		self.res = 0
		if not root:
			return self.res
		self.dfs(root, root.val, root.val)
		return int(self.res)


if __name__ == '__main__':
	root = Node(8, Node(3, Node(1), Node(6, Node(4), Node(7))), Node(10, None, Node(14, Node(13))))
	s = Solution()
	print s.maxAncestorDiff(root)
