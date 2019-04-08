# encoding=utf-8

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        Input: [2,1,5,6,2,3]
        Output: 10
        :type heights: List[int]
        :rtype: int
        升序栈
        所以top比top-1和i元素都大
        计算一次面积=top * i-（top-1）-1
        """
        stack = []
        res = 0
        heights = [0] + heights + [0]
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                th = heights[stack.pop()]
                left = stack[-1]
                res = max(res, th * (i - left - 1))
            stack.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    print s.largestRectangleArea([2, 1, 5, 6, 2, 3])
