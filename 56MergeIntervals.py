# encoding=utf-8

"""

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""


def mycmp(a, b):
	return a[0] - b[0]


class Solution(object):
	def merge(self, intervals):
		if not intervals:
			return []
		res = []
		starts = [0] * len(intervals)
		ends = [0] * len(intervals)
		for i, v in enumerate(intervals):
			starts[i] = v[0]
			ends[i] = v[1]
		starts.sort()
		ends.sort()
		j = 0
		for i in range(len(intervals)):
			if i == (len(intervals) - 1) or starts[i + 1] > ends[i]:
				res.append([starts[j], ends[i]])
				j = i + 1
		return res

	def merge2(self, intervals):
		"""
		:type intervals: List[List[int]]
		:rtype: List[List[int]]
		"""
		if not intervals:
			return []
		intervals.sort(cmp=mycmp)
		i = 0
		t = intervals[i]
		res = []
		while i < len(intervals) - 1:
			if t[1] >= intervals[i + 1][0]:
				if t[1] >= intervals[i + 1][1]:
					i += 1
					continue
				else:
					t[1] = intervals[i + 1][1]
			else:
				res.append(t)
				t = intervals[i + 1]
			i += 1
		res.append(t)
		return res


if __name__ == '__main__':
	s = Solution()
	print s.merge([[1, 4], [2, 3]])
