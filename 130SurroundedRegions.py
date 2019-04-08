class Solution(object):

	def ij2index(self, i, j):
		return i * self.col_len + j

	def root(self, index):
		while index != self.ida[index]:
			self.ida[index] = self.ida[self.ida[index]]
			index = self.ida[index]
		return index

	def union(self, p, q):
		rp = self.root(p)
		rq = self.root(q)
		if self.sz[rp] > self.sz[rq]:
			if self.inboarder[rq]:
				self.inboarder[rp] = True
			self.ida[rq] = rp
			self.sz[rp] += self.sz[rq]
			return rp
		else:
			if self.inboarder[rp]:
				self.inboarder[rq] = True
			self.ida[rp] = rq
			self.sz[rq] += self.sz[rp]
			return rq

	def inboard(self, i, j):
		if i == 0 or j == 0 or i == (self.row_len - 1) or j == (self.col_len - 1):
			self.inboarder[self.ij2index(i, j)] = 1

	def add(self, i, j):
		index = self.ij2index(i, j)
		# add top and left
		# top
		a, b = i - 1, j
		if a >= 0 and b >= 0:
			if self.board[a][b] == 'O':
				self.union(index, self.ij2index(a, b))

		# left
		a, b = i, j - 1
		if a >= 0 and b >= 0:
			if self.board[a][b] == 'O':
				self.union(index, self.ij2index(a, b))

	def solve(self, board):
		if not board or not board[0]:
			return
		self.board = board
		self.ida = []
		self.row_len = len(board)
		self.col_len = len(board[0])
		self.ida = [self.ij2index(i, j) for i in range(self.row_len) for j in range(self.col_len)]
		self.sz = [1 for i in range(self.row_len) for j in range(self.col_len)]
		self.inboarder = [0 for i in range(self.row_len) for j in range(self.col_len)]
		for i in range(self.row_len):
			for j in range(self.col_len):
				if board[i][j] == 'X':
					continue
				self.inboard(i, j)
				self.add(i, j)
		for i in range(self.row_len):
			for j in range(self.col_len):
				if board[i][j] == 'X':
					continue
				if not self.inboarder[self.root(self.ij2index(i, j))]:
					board[i][j] = 'X'
		"""
		:type board: List[List[str]]
		:rtype: None Do not return anything, modify board in-place instead.
		"""


# if __name__ == "__main__":
# 	board = [
# 		["O","X","X","O","X"],
# 		["X","O","O","X","O"],
# 		["X","O","X","O","X"],
# 		["O","X","O","O","O"],
# 		["X","X","O","X","O"]
# 	]
# 	s = Solution()
# 	s.solve(board)
# 	print board
