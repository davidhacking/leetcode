class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if not T:
            return []
        stack = []
        res = [0] * len(T)
        for i, t in enumerate(T):
            if not stack:
                stack.append(i)
                continue
            if T[stack[-1]] >= t:
                stack.append(i)
                continue
            while stack and T[stack[-1]] < t:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res


if __name__ == "__main__":
    s = Solution()
    print s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
