# encoding=utf-8
import heapq


class Data:
	def __init__(self, key, freq, time_no):
		self.freq = freq
		self.time_no = time_no
		self.key = key

	def __cmp__(self, other):
		if self.freq > other.freq:
			return 1
		elif self.freq < other.freq:
			return -1
		else:
			return self.time_no - other.time_no

	def __str__(self):
		return str(self.key)


if __name__ == '__main__':
	heap = []
	heapq.heappush(heap, Data(0, 1, 1))
	heapq.heappush(heap, Data(1, 1, 2))
	heapq.heappush(heap, Data(2, 1, 3))
	print heapq.heappop(heap)
