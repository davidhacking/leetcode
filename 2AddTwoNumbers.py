# Definition for singly-linked list.
"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def __str__(self):
		res = ""
		cur = self
		while cur:
			res += str(cur.val) + "->"
			cur = cur.next
		return res


"""
"""


class Solution(object):
	def addTwoNumbers(self, l1, l2):
		res = cur = ListNode(0)
		carry = 0
		while l1 or l2 or carry:
			if l1:
				carry += l1.val
				l1 = l1.next
			if l2:
				carry += l2.val
				l2 = l2.next
			cur.next = ListNode(carry % 10)
			carry = carry / 10
			cur = cur.next
		return res.next


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
	print s.addTwoNumbers(l1, l2)
