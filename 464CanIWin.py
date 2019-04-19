# encoding=utf-8


class Solution(object):
	def helper(self, total):
		res = self.lookup.get(''.join(self.vector), None)
		if res is not None:
			return res
		for i in range(1, self.max_int + 1):
			if self.vector[i - 1] != '0':
				continue
			if i >= total:
				self.lookup[''.join(self.vector)] = True
				return True
			self.vector[i-1] = '1'
			flag = self.helper(total - i)
			self.lookup[''.join(self.vector)] = flag
			if not flag:
				self.vector[i - 1] = '0'
				return True
			self.vector[i - 1] = '0'
		return False

	def canIWin(self, maxChoosableInteger, desiredTotal):
		"""
		:type maxChoosableInteger: int
		:type desiredTotal: int
		:rtype: bool
		"""
		if maxChoosableInteger >= desiredTotal:
			return True
		if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
			return False
		self.max_int = maxChoosableInteger
		self.vector = ['0' for i in range(maxChoosableInteger)]
		self.lookup = {}
		return self.helper(desiredTotal)


if __name__ == '__main__':
	s = Solution()
	print s.canIWin(10, 20)
