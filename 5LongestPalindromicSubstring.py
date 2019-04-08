# encoding=utf-8
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        slen = len(s)
        res = ""
        reslen = 0
        dp = [[0] * slen for i in range(slen)]
        for i in range(slen):
            for j in range(0, i + 1):
                if s[i] == s[j] and (i - j + 1 <= 2 or dp[i - 1][j + 1]):
                    dp[i][j] = 1
                if dp[i][j] and i - j + 1 > reslen:
                    reslen = i - j + 1
                    res = s[j:i + 1]
        return res


if __name__ == '__main__':
    s = Solution()
    print s.longestPalindrome("cbbd")
