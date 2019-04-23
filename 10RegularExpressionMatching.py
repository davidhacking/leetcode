# encoding=utf-8

class Solution(object):
	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		'.' Matches any single character.
		'*' Matches zero or more of the preceding element
		"""
		dp = [[0 for j in range(len(p) + 1)] for i in range(len(s) + 1)]
		dp[0][0] = 1
		for i in range(len(p)):
			if p[i] == '*' and dp[0][i - 1]:
				dp[0][i + 1] = 1
		for i in range(len(s)):
			for j in range(len(p)):
				if s[i] == p[j] or p[j] == '.':
					dp[i + 1][j + 1] = dp[i][j]
				elif p[j] == '*':
					if s[i] == p[j - 1] or p[j - 1] == '.':
						dp[i + 1][j + 1] = dp[i + 1][j - 1] or dp[i + 1][j] \
										   or dp[i][j + 1]  # 多个的情况最难想，多个其实是舍弃掉i+1然后回退到i与j+1
					elif s[i] != p[j - 1]:
						dp[i + 1][j + 1] = dp[i + 1][j - 1]

		return dp[-1][-1]


if __name__ == '__main__':
	s = Solution()
	print s.isMatch("aa", "a*")
	print s.isMatch("ab", ".*")
