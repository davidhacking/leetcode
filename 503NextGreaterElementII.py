# encoding=utf-8


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        stack = []
        nums_len = len(nums)
        res = [0] * nums_len
        for i in range(2 * nums_len):
            real_index = i
            i = i % nums_len
            if not stack:
                stack.append(i)
                continue
            if nums[stack[-1]] < nums[i]:
                while stack and nums[stack[-1]] < nums[i]:
                    res[stack.pop()] = nums[i]
            if real_index < nums_len:
                stack.append(i)

        while stack:
            res[stack.pop()] = -1
        return res


if __name__ == '__main__':
    s = Solution()
    print s.nextGreaterElements([1, 2, 1])
