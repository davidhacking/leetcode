# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

"""
靠调试运行写出来的代码
写的时候纠结了一下初始化工作，每次都会纠结初始化时的代码和一般化的代码会有不一样的地方，想着两者能有一个代码就好了
高级语言没有引用类型也是挺麻烦的
测试用例自己没有好好琢磨下，导致收尾工作不够
"""
class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		r = None
		t = None
		s = 0
		while l1 is not None or l2 is not None:
			if r is None:
				r = ListNode(0)
				if l1 is not None:
					r.val += l1.val
					l1 = l1.next
				if l2 is not None:
					r.val += l2.val
					l2 = l2.next
				s = r.val / 10
				r.val = r.val % 10
				t = r
			else:
				t.next = ListNode(s)
				if l1 is not None:
					t.next.val += l1.val
					l1 = l1.next
				if l2 is not None:
					t.next.val += l2.val
					l2 = l2.next
				s = t.next.val / 10
				t.next.val = t.next.val % 10
				t = t.next
		if s > 0:
			t.next = ListNode(s)
		return r


def list2ListNode(lst):
	r = None
	t = None
	for i in lst[::-1]:
		if r is None:
			r = ListNode(i)
			t = r
		else:
			t.next = ListNode(i)
			t = t.next
	return r


if __name__ == "__main__":
	s = Solution()
	# l1 = list2ListNode([3, 4, 2])
	# l2 = list2ListNode([4, 6, 5])
	# s.addTwoNumbers(l1, l2)
	l1 = list2ListNode([5])
	l2 = list2ListNode([5])
	s.addTwoNumbers(l1, l2)
