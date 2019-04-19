# encoding=utf-8
"""
A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.

The world is modeled as a 2-D array of cells, where 0 represents uninfected cells,
and 1 represents cells contaminated with the virus.
A wall (and only one wall) can be installed between any two 4-directionally adjacent cells, on the shared boundary.

Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall.
Resources are limited. Each day, you can install walls around only one region
	-- the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night.
There will never be a tie.

Can you save the day? If so, what is the number of walls required?
If not, and the world becomes fully infected, return the number of walls used.

Example 1:
Input: grid =
[[0,1,0,0,0,0,0,1],
 [0,1,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,0]]
Output: 10
Explanation:
There are 2 contaminated regions.
On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:

[[0,1,0,0,0,0,1,1],
 [0,1,0,0,0,0,1,1],
 [0,0,0,0,0,0,1,1],
 [0,0,0,0,0,0,0,1]]

On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.

Example 2:
Input: grid =
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output: 4
Explanation: Even though there is only one cell saved, there are 4 walls built.
Notice that walls are only built on the shared boundary of two different cells.

Example 3:
Input: grid =
[[1,1,1,0,0,0,0,0,0],
 [1,0,1,0,1,1,1,1,1],
 [1,1,1,0,0,0,0,0,0]]
Output: 13
Explanation: The region on the left only builds two new walls.
Note:
The number of rows and columns of grid will each be in the range [1, 50].
Each grid[i][j] will be either 0 or 1.
Throughout the described process, there is always a contiguous viral region that will infect strictly more uncontaminated squares
	in the next round.

[[1]]
"""

from collections import defaultdict


class Solution(object):

	def init_union_list(self, p):
		if p not in self.union_list:
			self.union_list[p] = p
			self.size_root[p] = 1

	def root(self, p):
		self.init_union_list(p)
		while self.union_list[p] != p:
			self.union_list[p] = self.union_list[self.union_list[p]]
			p = self.union_list[p]
		return p

	def union(self, p1, p2):
		rp1 = self.root(p1)
		rp2 = self.root(p2)
		if rp1 == rp2:
			return
		if self.size_root[rp1] > self.size_root[rp2]:
			self.union_list[rp2] = rp1
			self.size_root[rp1] += self.size_root[rp2]
		else:
			self.union_list[rp1] = rp2
			self.size_root[rp2] += self.size_root[rp1]

	def check(self, x, y):
		if x < 0 or x >= self.row_num or y < 0 or y >= self.col_num:
			return False
		return True

	def add_union(self, i, j, x, y):
		if not (self.check(i, j) and self.check(x, y)):
			return
		if self.grid[x][y] == 1:
			self.union((i, j), (x, y))

	def add_danger(self, r, x, y):
		if not self.check(x, y):
			return
		if self.grid[x][y] == 0:
			self.danger_region[r].add((x, y))

	def neighbour(self, i, j):
		r = self.root((i, j))
		if r not in self.danger_region:
			self.danger_region[r] = set()

		if (i, j) in self.danger_region[r]:
			self.danger_region[r].discard((i, j))

		for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
			x, y = i + dx, j + dy
			self.add_union(i, j, x, y)
			self.add_danger(r, x, y)

	def save_point(self, r, x, y):
		if not self.check(x, y):
			return 0
		if self.grid[x][y] == 1 and self.root((x, y)) == r:
			return 1
		return 0

	def safe_point_neighbour(self, r, i, j):
		count = 0
		for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
			x, y = i + dx, j + dy
			count += self.save_point(r, x, y)
		return count

	def merge_danger_region(self):
		for p in self.danger_region.keys():
			r = self.root(p)
			if r == p:
				continue
			self.danger_region[r] = self.danger_region[r] | self.danger_region[p]
			self.danger_region.pop(p)
			self.danger_region[r] = self.danger_region[r] - self.expand_points

	def build_union(self):
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				if self.grid[i][j] != 1:
					continue
				t = (i, j)
				self.virus_set.add(t)
				if t not in self.union_list:
					self.union_list[t] = t
					self.size_root[t] = 1
				self.neighbour(i, j)
		self.merge_danger_region()

	def find_max_danger_root(self):
		mr = None
		max_num = 0
		for r in self.danger_region.keys():
			if max_num < len(self.danger_region[r]):
				max_num = len(self.danger_region[r])
				mr = r
		return mr

	def mark_kill_virus(self, r):
		for v in list(self.virus_set):
			if self.root(v) == r:
				self.virus_set.discard(v)
				self.danger_region[r].discard(v)
				self.grid[v[0]][v[1]] = 2
		self.danger_region.pop(r)

	def save_danger_area(self, r):
		for _, da in enumerate(self.danger_region[r]):
			self.res += self.safe_point_neighbour(r, da[0], da[1])
		self.mark_kill_virus(r)

	def expand_virus(self):
		self.expand_points = set()
		for r, pset in self.danger_region.items():
			for _, p in enumerate(pset):
				self.grid[p[0]][p[1]] = 1
				self.expand_points.add(p)
				self.virus_set.add(p)
		for _, p in enumerate(self.expand_points):
			self.neighbour(p[0], p[1])
		self.merge_danger_region()

	def containVirus(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		union find 病毒区域 union_list

		while 判断是否病毒已经被清除，清除return
			找到最大的病毒区域
			对最大的病毒区域用防护板隔开，同时计数，并标记为2
			扩大剩余的所有病毒区域，这个可以迭代

		union find 病毒区域
			通过建立并查集

		找最大的病毒区域
			遍历grid中的所有元素，find(node) not in safe_region
			在建立并查集的时候同时建立这块病毒的下一次感染区域（感染区域可能相互叠加）
			{
				病毒根节点：set(感染区域标记)
			}
			pop and add new？

		构造防护网后对并查集的治愈区域标记
			用一个set记录已经治愈的病毒区域 safe_region

		扩大剩余的所有病毒区域，增加union关系，并更新感染区域（两个数据结构关系）

		每次建立防护网需要的防护网数目
			对当前预期的所有下一个会被感染的点先判断四个方向是不是一个病毒区域，如果是则记录一次这个点已经加过了

		判断病毒是否被清除了，或全世界都被感染了
			记录当前病毒的数目和被清除病毒的数目，如果当前病毒数为all(grid)则表示全世界被感染了，如果被清除的病毒等于当前病毒数，则成功
		"""
		self.grid = grid
		self.col_num = len(grid[0])
		self.row_num = len(grid)
		self.all_num = self.col_num * self.row_num
		self.union_list = {}
		self.safe_region = {}
		self.danger_region = defaultdict(set)
		self.size_root = {}
		self.virus_set = set()
		self.res = 0
		self.expand_points = set()
		self.build_union()
		while not (not self.virus_set or len(self.virus_set) >= self.all_num):
			# print ''
			# print '\n'.join([str(row) for row in self.grid])
			max_danger_region = self.find_max_danger_root()
			if len(self.danger_region[max_danger_region]) <= 0:
				break
			self.save_danger_area(max_danger_region)
			self.expand_virus()
		return self.res


if __name__ == '__main__':
	"""
	[[1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0],
	  [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
	  [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
	  [1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
	  [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
	  [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0],
	  [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
	  [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0],
	  [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
	  [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
	  [1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
	  [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1],
	  [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1],
	  [1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
	  [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
	  [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
	  [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
	  [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1],
	  [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
	  [0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0]]
	运行成
	[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0]
	[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 0]
	[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2]
	[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 1, 2]
	[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 1, 1, 2]
	[2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 0, 2, 1, 1, 1]
	[2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 1, 1, 1]
	[2, 2, 0, 2, 2, 2, 0, 0, 2, 2, 2, 2, 0, 2, 2, 2, 1, 1, 1, 1]
	[2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 0, 2, 0, 2, 1, 1, 1, 2, 2]
	[2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 1, 2, 2, 2]
	[2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2, 0, 2]
	[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2]
	[2, 2, 2, 2, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2]
	[2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2]
	[2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0]
	[2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 2, 2, 2, 2, 0, 0, 0, 0]
	[2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2, 0, 0, 2]
	[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2]
	[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
	[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0]
	之后无法处理1被二围起来的情况
	"""
	s = Solution()
	print s.containVirus([[1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0],
						  [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
						  [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
						  [1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
						  [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
						  [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0],
						  [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
						  [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0],
						  [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
						  [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
						  [1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
						  [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1],
						  [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1],
						  [1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
						  [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
						  [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
						  [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
						  [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1],
						  [0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
						  [0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0]])
