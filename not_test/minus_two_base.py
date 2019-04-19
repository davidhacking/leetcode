# encoding=utf-8

"""
输出负2进制的数
"""


class Solution:
	def minus_two_base(self, num):
		# num > 0
		res = []
		base = 2 # 变换base则可能余数为负
		while num:
			num, b = divmod(num, base)
			# base = -base
			num = -num # 保证偶数时为正，基数时为负，并且py的divmod保证余数的符号和base保持一致
			res.append(str(b))
		res.reverse()
		return res


if __name__ == '__main__':
	s = Solution()
	print s.minus_two_base(10)
