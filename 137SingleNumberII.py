# encoding=utf-8

"""
http://www.elecfans.com/analog/20171120582266.html
真值表反推方法
a b n Ya Yb
0 0 0 0  0
0 0 1 0  1 b=~a & ~b &n | ~a & b & ~n

0 1 0 0  1
0 1 1 1  0 a=~a&b&n | a&~b&~n

1 0 0 1  0
1 0 1 0  0
"""


class Solution(object):
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		a, b = 0, 0
		for n in nums:
			t = (~a & b & n) | (a & ~b & ~n)
			b = (~a & ~b & n) | (~a & b & ~n)
			a = t
		return b


if __name__ == '__main__':
	s = Solution()
	print s.singleNumber([2, 2, 6, 2])
