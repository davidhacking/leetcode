# encoding=utf-8
from collections import defaultdict
import bisect, math


#
# class Solution:
#     def countPalindromicSubsequences(self, S):
#         from collections import defaultdict
#         import bisect
#         M = 1000000007
#         characters = defaultdict(list)
#         for idx, s in enumerate(S):
#             characters[s].append(idx)
#         lookup = {}
#         def helper(i, j):
#             if i >= j: return 0
#             if (i, j) in lookup:
#                 return lookup[(i, j)]
#             res = 0
#             for c, v in characters.items():
#                 # print(c)
#                 n = len(v)
#                 new_i = None
#                 new_j = None
#                 idx_i = bisect.bisect_left(v,i)
#                 if idx_i < n:
#                     new_i = v[idx_i]
#                 if new_i == None or new_i >= j: continue
#                 idx_j = bisect.bisect_left(v,j)-1
#                 new_j = v[idx_j]
#                 res += helper(new_i + 1, new_j) + 2 if new_i != new_j else 1
#             lookup[(i, j)] = res % M
#             return lookup[(i, j)]
#         return helper(0, len(S))


class Solution(object):
    def helper(self, i, j):
        if i >= j:
            return 0
        if (i, j) in self.lookup:
            return self.lookup[(i, j)]
        res = 0
        for c, cl in self.chars.items():
            x = bisect.bisect_left(cl, i)
            if x >= len(cl) or cl[x] >= j:
                continue
            y = bisect.bisect_left(cl, j) - 1  # 这里为什么-1，因为一开始传入的j是len，后续传入的cl[y]有不能重复计算，所以这样取值兼容了两种情况
            res += self.helper(cl[x] + 1, cl[y]) + 2 if cl[x] != cl[y] else 1
        self.lookup[(i, j)] = res % self.mod
        return self.lookup[(i, j)]

    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        self.S = S
        self.slen = len(S)
        self.lookup = {}
        self.mod = int(math.pow(10, 9) + 7)
        self.chars = defaultdict(list)
        for i, c in enumerate(S):
            self.chars[c].append(i)
        return self.helper(0, len(S))


if __name__ == '__main__':
    s = Solution()
    print s.countPalindromicSubsequences("bccb")
