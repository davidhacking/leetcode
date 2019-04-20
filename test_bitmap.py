# encoding=utf-8

import math


class Bitmap:
	# 一个int只使用32位用于存储，64为python也使用32位
	bits_len = 32

	def __init__(self, max_num):
		self.size = int(math.ceil(float(max_num) / Bitmap.bits_len))
		self.bit_map = [0 for i in range(self.size)]

	def get_map_index(self, num):
		index = int(math.ceil(float(num) / Bitmap.bits_len))
		return index - 1

	def get_bit_index(self, num):
		return num - self.get_map_index(num) * Bitmap.bits_len - 1

	def set_num(self, num, f=1):
		index = self.get_map_index(num)
		bitn = self.get_bit_index(num)
		if f:
			self.bit_map[index] |= f << bitn
		else:
			self.bit_map[index] &= ~(1 << bitn)

	def exist_num(self, num):
		index = self.get_map_index(num)
		bitn = self.get_bit_index(num)
		return True if self.bit_map[index] & (1 << bitn) else False


if __name__ == '__main__':
	bitmap = Bitmap(64)
	bitmap.set_num(1, 1)
	print bitmap.exist_num(1)
	bitmap.set_num(1, 0)
	print bitmap.exist_num(1)
	bitmap.set_num(64, 1)
	print bitmap.exist_num(64)
	bitmap.set_num(64, 0)
	print bitmap.exist_num(64)
