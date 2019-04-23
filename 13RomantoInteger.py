# encoding=utf-8

class Solution(object):
	def __init__(self):
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
		self.roman_dict = {}
		for i in self.roman_num:
			self.roman_dict[i[0]] = i[1]

	def romanToInt(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		i = 0
		res = 0
		while i < len(s):
			if i <= len(s) - 2:
				t = s[i:i + 2]
				if t in self.roman_dict:
					res += self.roman_dict[t]
					i += 2
					continue
			t = s[i:i + 1]
			res += self.roman_dict[t]
			i += 1
		return res


if __name__ == '__main__':
	s = Solution()
	print s.romanToInt("IV")
	print s.romanToInt("MCMXCIV")
	print s.romanToInt("XXXI")
	print s.romanToInt("XLI")
	print s.romanToInt("LXXXI")
