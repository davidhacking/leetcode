# encoding=utf-8
from collections import Counter


def counter_eq(counter1, counter2):
	keys1 = counter1.keys()
	keys2 = counter2.keys()
	if len(keys1) != len(keys2):
		return False
	for key in keys1:
		if counter1[key] != counter2[key]:
			return False
	return True


if __name__ == '__main__':
	counter1 = Counter()
	counter2 = Counter()
	counter1['c'] += 1
	counter2['c'] += 1
	print counter_eq(counter1, counter2)
	print counter1 == counter2
