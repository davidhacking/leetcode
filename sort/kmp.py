# encoding=utf-8

def search(s, keyword):
	kw_dict = handle_keyword(keyword)
	ret = []
	index = 0
	i = 0
	while i < len(s):
		flag = True
		while index < len(keyword):
			if i >= len(s) or keyword[index] != s[i]:
				flag = False
				break
			index += 1
			i += 1
		if flag:
			ret.append(i-index)
			index = 0
			continue
		else:
			if index == 0:
				i += 1
		index -= index - kw_dict[index-1]
	return ret


def handle_keyword(keyword):
	if not keyword:
		return
	kw_dict = {-1:0}
	for i, c in enumerate(keyword):
		count = 0
		for j in range(i - 1, -1, -1):
			if keyword[:j + 1] == keyword[i - j:i + 1]:
				count = j + 1
				break
		kw_dict[i] = count
	return kw_dict


if __name__ == "__main__":
	s = "BBC ABCDAB ABCDABCDABDE"
	keyword = "ABCDABD"
	# print handle_keyword(s)
	print search(s, keyword)