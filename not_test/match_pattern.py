# encoding=utf-8

def is_upper(c):
	return ord(c) >= ord('A') and ord(c) <= ord('Z')


class Solution:
	def handle_pattern(self):
		i, j = 0, 1
		self.patterns = []
		while i < len(self.pattern) and j <= len(self.pattern):
			if j == len(self.pattern) or is_upper(self.pattern[j]):
				self.patterns.append((i, j))
				i = j
			j += 1

	def match_pattern(self, i, pi):
		if pi < len(self.patterns):
			plen = self.patterns[pi][1] - self.patterns[pi][0]
			return self.qstr[i:i + plen] == self.pattern[self.patterns[pi][0]:self.patterns[pi][1]]
		return False

	def solve(self, queries, pattern):
		self.queries = queries
		self.pattern = pattern
		self.handle_pattern()
		print self.patterns
		res = []
		for qstr in queries:
			flag = True
			pi = -1
			self.qstr = qstr
			for i, c in enumerate(qstr):
				if is_upper(c):
					pi += 1
					if not self.match_pattern(i, pi):
						flag = False
						break
			if pi != len(self.patterns) - 1:
				flag = False
			res.append(flag)
		return res


if __name__ == '__main__':
	s = Solution()
	print s.solve(["FooBarTddd", 'FooBarTest', 'FooBaT'], "FooBaT")
