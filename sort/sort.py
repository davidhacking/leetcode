#encoding=utf-8


def get_min(arr, start, end):
	ret = 0
	min_value = None
	for index in range(start, end + 1):
		value = arr[index]
		if not min_value or min_value > value:
			min_value = value
			ret = index
	return ret


def bubble(arr):
	if not arr:
		return arr
	for i in range(0, len(arr)):
		min_value_index = get_min(arr, i, len(arr) - 1)
		t = arr[i]
		arr[i] = arr[min_value_index]
		arr[min_value_index] = t
	return arr


def merge(arr, a, b, x, y):
	i = a
	j = x
	while i <= y and j <= y:
		if arr[i] > arr[j]:
			t = arr[i]
			arr[i] = arr[j]
			arr[j] = t
		i += 1
	return arr


def _quick_sort_recursion(arr, start, end):
	if start > end:
		return


def quick_sort_recursion(arr):
	_quick_sort_recursion(arr, 0, len(arr) / 2)
	_quick_sort_recursion(arr, len(arr) / 2 + 1, len(arr) - 1)


def quick_sort(array, left, right):
	if left >= right:
		return
	low = left
	high = right
	key = array[low]
	while left < right:
		while left < right and array[right] > key:
			right -= 1
		array[left] = array[right]
		while left < right and array[left] <= key:
			left += 1
		array[right] = array[left]
	array[right] = key
	quick_sort(array, low, left - 1)
	quick_sort(array, left + 1, high)


def patition(array, s, e, x=0):
	array[e], array[x] = array[x], array[e]
	k = -1  # 用于记录k+1就是第一个大于array[x]的数，即保证前k个数都小于array[x]
	for i in range(s, e):
		if array[i] <= array[e]:
			k += 1
			array[i], array[k] = array[k], array[i]
	k += 1
	array[k], array[e] = array[e], array[k]
	return k


def patition2(array, s, e, x=0):
	# 右边找一个数小于等于array[x]的换到左边
	# 左边找一个数大于array[x]的换到右边
	# 一直做，直到左右相遇
	if s > e:
		return -1
	key = array[x]
	left = s
	right = e
	array[s], array[x] = array[x], array[s]

	while left < right:
		while left < right and array[right] > key:
			right -= 1
		array[left] = array[right]
		while left < right and array[left] <= key:
			left += 1
		array[right] = array[left]
	array[right] = key
	return right


if __name__ == "__main__":
	a = [7, 2, 6, 3, 7, 10]
	# quick_sort(a, 0, len(a) - 1)
	print patition2(a, 0, len(a) - 1, 1)
	print a
