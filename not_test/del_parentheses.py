# encoding=utf-8

class Solution:
	def solve(self, data):
		res = []
		not_print_set = set()
		stack = []
		for i, c in enumerate(data):
			if c != ')':
				stack.append(i)
			elif c == ')':
				while stack and data[stack[-1]] != '(':
					stack.pop()
				last = stack.pop()
				if not stack:
					not_print_set.add(last)
					not_print_set.add(i)
		for i, c in enumerate(data):
			if i not in not_print_set:
				res.append(c)
		return ''.join(res)

	def solve2(self, data):
		res = []
		opened = 0
		for _, c in enumerate(data):
			if c == '(':
				opened += 1
			elif c == ')':
				opened -= 1
			if opened > 0:
				if opened == 1 and c == '(':
					continue
				res.append(c)
		return ''.join(res)


if __name__ == '__main__':
	data = "(()())(())"
	s = Solution()
	print s.solve(data)
	print s.solve2(data)
