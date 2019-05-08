# encoding=utf-8

"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK.
Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries,
you should return the itinerary that has the smallest lexical order when read as a single string.
For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""


def cmp(i, j):
	if i[1] > j[1]:
		return 1
	elif i[1] < j[1]:
		return -1
	return 0


class Solution(object):
	def findItinerary(self, tickets):
		"""
		:type tickets: List[List[str]]
		:rtype: List[str]
		"""
		from collections import defaultdict
		data = defaultdict(list)
		tickets.sort(cmp)
		for a, b in tickets[::-1]:
			data[a].append(b)
		res = []
		cur = "JFK"
		def visit(node):
			if len(data[node]) > 0:
				t = data[node].pop()
				res.append(t)
				visit(t)

		res.append(cur)
		while len(data[cur]) > 0:
			visit(cur)
		return res


if __name__ == '__main__':
	s = Solution()
	print s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]) #["JFK","NRT","JFK","KUL"]
	# print s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]) #["JFK","ATL","JFK","SFO","ATL","SFO"]
