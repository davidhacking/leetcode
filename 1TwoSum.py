# encoding=utf-8

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class IndexCmp:
	def __init__(self, arr):
		self.arr = arr

	def __call__(self, a, b):
		return self.arr[a] - self.arr[b]


class Solution(object):

	def twoSum(self, nums, target):
		# 利用find的方式
		lookup = {}
		for i, n in enumerate(nums):
			if target-n in lookup:
				return [i, lookup[target-n]]
			lookup[n] = i

	def twoSum2(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		index_list = [i for i in range(len(nums))]
		index_cmp = IndexCmp(nums)
		index_list.sort(index_cmp)
		left = 0
		right = len(nums) - 1
		while left < right:
			t = nums[index_list[left]] + nums[index_list[right]]
			if t > target:
				right -= 1
			elif t < target:
				left += 1
			else:
				if index_list[left] > index_list[right]:
					return [index_list[right], index_list[left]]
				else:
					return [index_list[left], index_list[right]]


if __name__ == '__main__':
	s = Solution()
	print s.twoSum([3, 2, 4], 6)
