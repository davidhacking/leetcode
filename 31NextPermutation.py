# encoding=utf-8


"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution(object):
	def nextPermutation(self, nums):
		"""
		:type nums: List[int]
		:rtype: None Do not return anything, modify nums in-place instead.
		1. 找降序i ai < a(i+1)
		2. 从i+1到len-1找第一个比ai大的数和ai交换
		3. 重新排序i+1到len-1
		"""
		i = len(nums) - 1
		x = -1
		while i - 1 >= 0:
			if nums[i - 1] < nums[i]:
				x = i - 1
				break
			i -= 1
		if x == -1:
			nums.reverse()
			return False
		j = x+1
		y = -1
		while j < len(nums) and nums[j] > nums[x]:
			y = j
			j += 1
		nums[x], nums[y] = nums[y], nums[x]
		t = nums[x + 1:]
		t.sort()
		for k in range(x + 1, len(nums)):
			nums[k] = t[k - x - 1]
		return True


if __name__ == '__main__':
	s = Solution()
	nums = [1, 2, 3, 4]
	while s.nextPermutation(nums):
		print nums
