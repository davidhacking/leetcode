"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR" PAHNAPLSIIGYIR
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


# encoding=utf-8

class Solution(object):
	def helper(self, i, nr):
		for k in range(i, i + nr):
			self.index[k - i].append(k)
		for k in range(i + nr, i + nr + nr - 2):
			self.index[nr - 1 - (k - i - nr) - 1].append(k)

	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		if numRows <= 1:
			return s
		self.index = [[] for i in range(numRows)]
		for k in range(0, len(s), 2 * numRows-2):
			self.helper(k, numRows)
		self.res = []
		for _, row in enumerate(self.index):
			for i in row:
				if i < len(s):
					self.res.append(s[i])
		return ''.join(self.res)


if __name__ == '__main__':
	s = Solution()
	print s.convert("PAYPALISHIRING", 2)
