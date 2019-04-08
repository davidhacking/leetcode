# encoding=utf-8

"""
用时1h，写了半小时，调试了半小时
"""

class Solution(object):
    def canAdditive(self, start, end, i, j):
        if j > end + 1: return False
        t = i + (end - i + 1) / 2 + 1
        if i >= j or j > t: return False
        if (self.num[i] == '0' and j - i > 1) or (self.num[start] == '0' and i - start > 1):
            return self.canAdditive(start, end, i + 1, j + 1)
        a = int(self.num[start:i])
        for j in range(j, t + 1):
            if self.num[i] == '0' and j - i > 1:
                continue
            b = int(self.num[i:j])
            cstr = str(a + b)
            if cstr == self.num[j:j + len(cstr)]:
                if j + len(cstr) == len(self.num):
                    return True
                else:
                    flag = self.canAdditive(i, end, j, j + len(cstr))
                    if flag: return True
        return self.canAdditive(start, end, i + 1, i + 2)

    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        self.num = num
        if len(self.num) < 3:
            return False
        return self.canAdditive(0, len(self.num) - 1, 1, 2)


if __name__ == '__main__':
    s = Solution()
    """
    "1023"
    "000"
    "101"
    "211738"
    """
    print s.isAdditiveNumber("211738")
