# encoding=utf-8

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        slen = len(s)
        res = 0
        if slen <= 0: return res
        dp = [[0] * slen for i in range(slen)]
        for i in range(slen):
            for j in range(0, i + 1):
                if s[i] == s[j] and (i - j + 1 <= 2 or dp[i - 1][j + 1]):
                    dp[i][j] = 1
                    res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print s.countSubstrings("aaa")
