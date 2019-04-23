# encoding=utf-8

"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Example 1:

Input: 3
Output: "III"

Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


def between(n, a, b):
	if a <= n <= b:
		return True
	return False


class Solution(object):
	def __init__(self):
		self.roman = {
			'I': 1,
			'V': 5,
			'X': 10,
			'L': 50,
			'C': 100,
			'D': 500,
			'M': 1000,
		}
		self.roman_num = [
			('M', 1000),
			('CM', 900),
			('D', 500),
			('CD', 400),
			('C', 100),
			('XC', 90),
			('L', 50),
			('XL', 40),
			('X', 10),
			('IX', 9),
			('V', 5),
			('IV', 4),
			('I', 1),
		]

	def helper(self, num, a, b, c):
		"""
		:type num: int
		:type a: str
		:type b: str
		:type c: str
		:rtype: str
		"""
		if num >= self.roman[a]:
			return a + self.intToRoman(num - self.roman[a])
		elif between(num, self.roman[b], self.roman[a]):
			if between(num, self.roman[b], self.roman[a] - self.roman[c] - 1):
				cn = (num - self.roman[b]) / self.roman[c]
				return b + (c * cn) + self.intToRoman(num - self.roman[b] - self.roman[c] * cn)
			else:
				return c + a + self.intToRoman(num - (self.roman[a] - self.roman[c]))
		elif between(num, self.roman[c], self.roman[b]):
			if between(num, self.roman[c], self.roman[b] - self.roman[c] - 1):
				cn = num / self.roman[c]
				return c * cn + self.intToRoman(num - self.roman[c] * cn)
			else:
				return c + b + self.intToRoman(num - (self.roman[b] - self.roman[c]))
		return False

	def intToRoman2(self, num):
		"""
		:type num: int
		:rtype: str
		"""
		if num == 0:
			return ""
		for a, b, c in [('M', 'D', 'C'), ('C', 'L', 'X'), ('X', 'V', 'I'), ]:
			res = self.helper(num, a, b, c)
			if res:
				return res

	def intToRoman(self, num):
		res = ""
		for i in self.roman_num:
			if num >= i[1]:
				t = num / i[1]
				res += i[0] * t
				num -= t * i[1]
		return res



if __name__ == '__main__':
	s = Solution()
	print s.intToRoman(1)
	print s.intToRoman(3)
	print s.intToRoman(4)
	print s.intToRoman(9)
	print s.intToRoman(58)
	print s.intToRoman(1994)
	print s.intToRoman(31)
	print s.intToRoman(41)
	print s.intToRoman(81)
