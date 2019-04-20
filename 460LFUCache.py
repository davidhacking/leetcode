# encoding=utf-8

"""
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item.
For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency),
the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4


算法：
需要做到两个维度的查询：
1. 按使用次数
2. 按插入顺序
次数，使用dict
插入顺序，使用ordered dict（pop的使用last=False就是弹出最早插入的）
按照优先级构建dict数据结构

key->value,f 再用一个dict数据结构

技巧：
	插入时，先插入，再判断当前是否需要弹出元素，如果要则紧接着弹出，就省去了很多判断

评价：
	这个做法完全利用的是OrderedDict的特性，即能在O(1)时间找到key又能利用popitem(last=False)按FIFO的原则删除元素
	所以OrderedDict是怎么实现的？OrderedDict本身就是一个dict+双向链表实现的，dict里记录了key->node，双向链表记录了node(key)
	popitem时用双向链表pop，OrderedDict本身就是一个LRU算法
"""

from collections import defaultdict, OrderedDict


class Data:
	def __init__(self, value, freq):
		self.freq = freq
		self.value = value

	def __str__(self):
		return str(self.value)


class LFUCache(object):

	def __init__(self, capacity):
		"""
		:type capacity: int
		"""
		self.remain = capacity
		self.query_dict = defaultdict(OrderedDict)
		self.least_use_freq = 1
		self.cache = {}

	def _update(self, key, value=None):
		data = self.cache.pop(key)
		if value:
			data.value = value
		self.query_dict[data.freq].pop(key)
		# 检查弹出的item使得使用次数最少的list为空，则表示是这个key引起的，而下一次item的freq会++，所以这里也需要++
		if len(self.query_dict[self.least_use_freq]) == 0:
			self.least_use_freq += 1
		data.freq += 1
		self.cache[key] = data
		self.query_dict[data.freq][key] = data.value

	def get(self, key):
		"""
		:type key: int
		:rtype: int
		"""
		if key not in self.cache:
			return -1
		self._update(key)
		return self.cache[key].value

	def put(self, key, value):
		"""
		:type key: int
		:type value: int
		:rtype: None
		"""
		if key in self.cache:
			self._update(key, value)
			return
		data = Data(value, 1)
		self.cache[key] = data
		self.query_dict[data.freq][key] = value
		if self.remain > 0:
			self.remain -= 1
		else:
			key, _ = self.query_dict[self.least_use_freq].popitem(last=False)
			self.cache.pop(key)
		# 先做弹出操作，再改变最少的频率，因为需要remove的item是最先插入的item
		self.least_use_freq = 1


# class LFUCache(object):
# 	def __init__(self, capacity):
# 		self.remain = capacity
# 		self.nodesForFrequency = defaultdict(OrderedDict)
# 		self.leastFrequency = 1
# 		self.nodeForKey = {}
#
# 	def _update(self, key, newValue=None):
# 		value, freq = self.nodeForKey[key]
# 		if newValue is not None: value = newValue
# 		self.nodesForFrequency[freq].pop(key)
# 		if len(self.nodesForFrequency[self.leastFrequency]) == 0: self.leastFrequency += 1
# 		self.nodesForFrequency[freq + 1][key] = (value, freq + 1)
# 		self.nodeForKey[key] = (value, freq + 1)
#
# 	def get(self, key):
# 		if key not in self.nodeForKey: return -1
# 		self._update(key)
# 		return self.nodeForKey[key][0]
#
# 	def put(self, key, value):
# 		if key in self.nodeForKey:
# 			self._update(key, value)
# 		else:
# 			self.nodeForKey[key] = (value, 1)
# 			self.nodesForFrequency[1][key] = (value, 1)
# 			if self.remain == 0:
# 				removed = self.nodesForFrequency[self.leastFrequency].popitem(last=False)
# 				self.nodeForKey.pop(removed[0])
# 			else:
# 				self.remain -= 1
# 			self.leastFrequency = 1  # should be one after adding a new item


if __name__ == '__main__':
	cache = LFUCache(0)

	cache.put(0, 0)
	print cache.get(0)
