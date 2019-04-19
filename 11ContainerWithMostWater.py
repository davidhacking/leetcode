# encoding=utf-8
"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate
(i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.
真tm有意思，双指针法，我真是没啥好想法，然后硬写出来的
双指针法+随便一个条件
"""


class Solution(object):
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		res = 0
		if not height:
			return res
		left = 0
		right = len(height) - 1
		while left < right:
			t = (right - left) * min(height[right], height[left])
			res = max(t, res)
			if height[right] > height[left]:
				left += 1
			else:
				right -= 1
		return res


if __name__ == '__main__':
	s = Solution()
	print s.maxArea([6, 4, 6, 2, 5, 4, 8, 3, 5])
