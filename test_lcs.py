# encoding=utf-8


def lcs(A, B):
	dp = [[0] * (len(A) + 1) for i in range(len(B) + 1)]
	for i, a in enumerate(A):
		for j, b in enumerate(B):
			if a == b:
				dp[i + 1][j + 1] = dp[i][j] + 1
			else:
				dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
	return dp[-1][-1]


if __name__ == '__main__':
	print lcs("ABCD", "EACB")
