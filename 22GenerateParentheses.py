# encoding=utf-8
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
生成有效括号对问题，其实是一个卡塔兰数问题(Catalan)
分而治之的思想：
1. f(n)表示n对括号的所有有效括号解决方案
2. 如果需要求f(n)那我们其实可以先求f(0)到f(n-1)
3. 对于在第k个位置增加括号的问题，此时，我们只能加括号成这个样子'(' f(k-1) ')' f(n-k)，
	a.如果加成这样'()' f(k-1) f(n-k) 就会和k=0位置加括号 '()' f(k-2) '()' f(n-k)情况重复
	b.如果加在中间 f(k-1) '()' f(n-k) 就会和k=0位置加括号 '()' f(k-2) '()' f(n-k)情况重复
	c.如果加在中间 f(k-1) '(' f(n-k) ')' 就会和k-1位置加括号 '(' f(k-2) '())(' f(n-k-1) ')'情况重复
	d.如果加在中间 f(k-1) f(n-k) '()' 就会和在第k-2位置加括号 '(' f(k-2) ')' f(n-k-1) '()'情况重复
	所以，只有一种加括号的方式
4. k可以出现在0-n的任何一个位置，所以f(n) = SUM(for k from 1 to n) f(k-1)f(n-k)种解决方案

如果不考虑有效无效（一下属于推测未验证）
f(n) = SUM(for k from 1 to n) [f(k-1)f(n-k) - 0 if n为基数 else f(n/2)]
"""

from collections import Counter


class Solution(object):

	def __init__(self):
		self.res_dict = {0: ['']}

	def generateParenthesis(self, n):
		"""
		:type n: int
		:rtype: List[str]
		这个算法居然打败了97%的人，简直了，所以算法还是需要有深厚的数学基础，这样写出来的代码才效率高
		"""
		if n in self.res_dict:
			return self.res_dict[n]
		self.res_dict[n] = []
		for k in range(1, n+1):
			parts1 = self.generateParenthesis(k - 1)
			parts2 = self.generateParenthesis(n - k)
			for i in parts1:
				for j in parts2:
					self.res_dict[n].append('(' + i + ')' + j)
		return self.res_dict[n]


if __name__ == '__main__':
	s = Solution()
	print s.generateParenthesis(2)
