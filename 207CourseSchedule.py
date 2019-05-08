# encoding=utf-8

"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""

from collections import defaultdict


class Solution(object):
	def __init__(self):
		self.lookup = None
		self.data = None

	def help(self, numCourses, prerequisites, k, learning):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: bool
		"""
		if self.lookup[k] != -1:
			return self.lookup[k]
		learning[k] = 1
		for c in self.data[k]:
			if learning[c]:
				self.lookup[k] = 0
				return self.lookup[k]
			else:
				flag = self.help(numCourses, prerequisites, c, learning)
				if not flag:
					self.lookup[k] = 0
					return self.lookup[k]
		learning[k] = 0
		self.lookup[k] = 1
		return self.lookup[k]

	def canFinish(self, numCourses, prerequisites):
		self.lookup = [-1] * numCourses  # 0 for not ok, 1 for ok
		self.data = defaultdict(list)
		for c in prerequisites:
			self.data[c[0]].append(c[1])
		for k in range(numCourses):
			learning = [0] * numCourses
			if not self.help(numCourses, prerequisites, k, learning):
				return False
		return True


if __name__ == '__main__':
	s = Solution()
	"""
	3
[[0,1],[0,2],[1,2]]
	"""
	# print s.canFinish(2, [[0, 1]])
	# print s.canFinish(2, [[0, 1], [1, 0]])
	print s.canFinish(3, [[0, 1], [0, 2], [1, 2]])
