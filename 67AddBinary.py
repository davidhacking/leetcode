class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        na = 0
        nb = 0
        c = 0
        left = 0
        res
        if a != "":
            na = 1 if a.pop() == '1' else 0
        if b != "":
            na = 1 if a.pop() == '1' else 0
        if na + nb == 2:
            c = 1
        """
        a = list(a)
        b = list(b)
        na, nb, c, left = 0, 0, 0, 0
        res = []
        while a or b:
            na = 1 if a and a.pop() == '1' else 0
            nb = 1 if b and b.pop() == '1' else 0
            t = na + nb + c
            c = t / 2
            left = t % 2
            res.append('0' if left == 0 else '1')
        if c:
            res.append('1')
        res.reverse()
        res = ''.join(res)
        return res


if __name__ == '__main__':
    s = Solution()
    print s.addBinary("111", '111')
