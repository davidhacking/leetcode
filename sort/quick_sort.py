# encoding=utf-8

def patition(array, start, end, x):
	array[start], array[x] = array[x], array[start]
	x = start
	left = start
	right = end
	while left < right:
		while array[right] >= array[x] and right > left:
			right -= 1
		array[right], array[x] = array[x], array[right]
		x = right
		while array[left] < array[x] and right > left:
			left += 1
		array[left], array[x] = array[x], array[left]
		x = left
	return left


def patition2(array, start, end, x):
	key = array[x]
	array[start], array[x] = array[x], array[start]
	k = start
	i = start + 1
	while i <= end:
		if key <= array[i]:
			k += 1
			array[k], array[i] = array[i], array[k]
		i += 1
	k += 1
	array[k] = key
	return k


def quick_sort(array, start=0, end=None):
	if end is None:
		end = len(array) - 1
	if start >= end:
		return
	mid = patition(array, start, end, start)
	quick_sort(array, start, mid - 1)
	quick_sort(array, mid + 1, end)


if __name__ == '__main__':
	a = [7, 2, 6, 3, 7, 10]
	print patition2(a, 0, len(a) - 1, 0)
	print a
	quick_sort(a)
	print a
