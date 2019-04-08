# encoding=utf-8

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        sort
        i j = 0 0
        while i <= j and j <= len:
            if numsj - numsi > k:
                i++
            else if nj - ni < k:
                j++
            else:
                res++
                j++
        """
        if not nums:
            return 0
        nums.sort()
        i, j = 0, 0
        last_num1, last_num2 = None, None
        res = 0
        while i <= j and j < len(nums):
            t = nums[j] - nums[i]
            if t > k:
                i += 1
            elif t < k:
                j += 1
            else:
                if i != j:
                    if (last_num1 is None and last_num2 is None) or (last_num1 != nums[i] and last_num2 != nums[j]):
                        res += 1
                        last_num1 = nums[i]
                        last_num2 = nums[j]
                j += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print s.findPairs([3, 1, 4, 1, 5], 2)
