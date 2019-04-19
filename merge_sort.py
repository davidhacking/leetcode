def merge_result(array, a, b, x, y):
	tmp = [0] * (b - a + 1 + y - x + 1)
	i, j = a, x
	k = 0
	while i <= b and j <= y:
		if array[i] <= array[j]:
			tmp[k] = array[i]
			i += 1
		else:
			tmp[k] = array[j]
			j += 1
		k += 1
	while i <= b:
		tmp[k] = array[i]
		i += 1
		k += 1
	while j <= y:
		tmp[k] = array[j]
		j += 1
		k += 1
	for t in tmp:
		array[a] = t
		a += 1


def merge_sort(array, s, e):
	if s >= e:
		return
	if s == (e - 1):
		if array[s] > array[e]:
			array[s], array[e] = array[e], array[s]
		return
	mid = int((s + e) / 2)
	merge_sort(array, s, mid)
	merge_sort(array, mid + 1, e)
	merge_result(array, s, mid, mid + 1, e)


def merge_sort_bottom_up(array, divider=1):
	if divider > len(array):
		return
	tmp = [i for i in array]
	for i in range(0, len(array), 2 * divider):
		a, b = i, i + divider
		for k in range(i, i + 2 * divider):
			if k >= len(array) or (a >= len(array) and b >= len(array)):
				break
			elif a >= i + divider or a >= len(array):
				array[k] = tmp[b]
				b += 1
			elif b >= i + 2 * divider or b >= len(array):
				array[k] = tmp[a]
				a += 1
			elif tmp[a] < tmp[b]:
				array[k] = tmp[a]
				a += 1
			elif tmp[a] >= tmp[b]:
				array[k] = tmp[b]
				b += 1
	merge_sort_bottom_up(array, divider * 2)


if __name__ == '__main__':
	s = [1, 3, 2, 4, -1]
	# merge_sort(s, 0, len(s) - 1)
	# print s
	import random
	for length in range(1, 20):
		array = [random.randint(0, 100) for i in range(length)]
		merge_sort_bottom_up(array)
		print array
