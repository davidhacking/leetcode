# encoding=utf-8

class Solution(object):
	def trap(self, heights):
		"""
		Input: [0,1,0,2,1,0,1,3,2,1,2,1]
		Output: 6
		:type heights: List[int]
		:rtype: int
		降序栈，从栈底忘栈顶看
		f(x)x所指向的元素，top-1表示弹出top后的下一个栈顶
		f(top)比f(top-1)和f(i)都小
		计算一次水量=(min(f(top-1),f(i))-f(top))*(i-(top-1))
		"""
		# 升序不管，降序管
		stack = []
		ret = 0
		for i, h in enumerate(heights):
			while stack and heights[stack[-1]] < h:
				mid = stack.pop()
				if not stack:
					break
				left = stack[-1]
				right = i
				ret += (min(heights[left], heights[right]) - heights[mid]) * (right - left - 1)
			stack.append(i)
		return ret


if __name__ == "__main__":
	s = Solution()
	print s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
