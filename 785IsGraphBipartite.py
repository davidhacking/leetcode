# encoding=utf-8

class Solution(object):
	# 需要自己初始化一次访问数组
	def get_not_visit(self):
		for i, v in enumerate(self.visit):
			if not v:
				return i
		return None

	def dfs(self, vertex):
		flag = 1
		if self.visit[vertex] == flag:
			flag = -flag
		for v in self.graph[vertex]:
			if not self.visit[v]:
				self.visit[v] = flag
				self.dfs(v)

	def isBipartite(self, graph):
		"""
		:type graph: List[List[int]]
		:rtype: bool
		"""
		if not graph or len(graph) <= 0:
			return True
		self.graph = graph
		self.visit = [0 for i in range(len(self.graph))]
		v = self.get_not_visit()
		while v is not None:
			self.visit[v] = -1
			self.dfs(v)
			v = self.get_not_visit()
		for i, vertexes in enumerate(self.graph):
			for v in vertexes:
				if self.visit[i] == self.visit[v]:
					return False
		return True


if __name__ == '__main__':
	s = Solution()
	"""
	[[1,4],[0,2],[1],[4],[0,3]] true
	"""
	print s.isBipartite([[1, 4], [0, 2], [1], [4], [0, 3]])
