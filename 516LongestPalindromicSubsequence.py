# encoding=utf-8

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        slen = len(s)
        res = 0
        dp = [[0] * slen for i in range(slen)]
        for i in range(slen):
            for j in range(i, -1, -1):
                if s[i] == s[j]:
                    if i - j + 1 <= 2:
                        dp[i][j] = i - j + 1
                    else:
                        dp[i][j] = dp[i - 1][j + 1] + 2
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j + 1])
                res = max(res, dp[i][j])
        return res


if __name__ == '__main__':
    s = Solution()
    print s.longestPalindromeSubseq("bbbab")
