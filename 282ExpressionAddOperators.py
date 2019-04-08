# encoding=utf-8


class Solution(object):
    def add_res(self):
        item = []
        for i, c in enumerate(self.ops):
            item.append(self.num[i])
            if c != 'x':
                item.append(c)
        self.res.append(''.join(item))

    def helper(self, left, cur, index):
        if index >= self.num_len and left + cur == self.target:
            self.add_res()
            return
        for i in range(index, self.num_len):
            self.ops[index - 1] = '-'
            self.helper(left + cur, -int(self.num[index:i + 1]), i + 1)
            self.ops[index - 1] = '+'
            self.helper(left + cur, int(self.num[index:i + 1]), i + 1)
            self.ops[index - 1] = '*'
            self.helper(left, cur * int(self.num[index:i + 1]), i + 1)
            self.ops[index - 1] = 'x'

            if self.num[index] == '0':
                break

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.res = []
        self.num = num
        self.target = target
        self.num_len = len(num)
        self.ops = ['x'] * self.num_len
        for i in range(self.num_len):
            self.helper(0, int(self.num[0:i + 1]), i + 1)
            if self.num[0] == '0':
                break
        return self.res


if __name__ == '__main__':
    s = Solution()
    """
    "105"
5
"123456789"
45
"1000000009"
9
    """
    for tmp in s.addOperators("1000000009", 9):
        print tmp, eval(tmp)
