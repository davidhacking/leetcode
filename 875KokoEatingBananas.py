# encoding=utf-8

class Solution(object):
	def minEatingSpeed(self, piles, H):
		"""
		:type piles: List[int]
		:type H: int
		:rtype: int
		"""
		if not piles:
			return 0
		piles.sort()
		import bisect, math
		left, right = math.ceil(float(sum(piles))/H), piles[-1]
		while left < right:
			k = left + (right - left) / 2
			i = bisect.bisect_left(piles, k)
			times = i
			for j in range(i, len(piles)):
				times += int(math.ceil(float(piles[j])/k))
			if times > H:
				left = k + 1
			else:
				right = k
		return int(left)


if __name__ == '__main__':
	s = Solution()
	"""
	[3,6,7,11], 8 4
	[30, 11, 23, 4, 20], 5 30
	[30, 11, 23, 4, 20], 6 23
	[332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589, 290818316, 877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184], 823855818 14
	[312884470], 968709470
	"""
	print s.minEatingSpeed([312884470], 968709470)
