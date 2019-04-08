# encoding=utf-8
class ListNode(object):
    def __init__(self, x):
        if type(x) is not list:
            self.val = x
            self.next = None
        else:
            curr = self
            for item in x:
                if not hasattr(curr, 'val'):
                    curr.val = item
                    curr.next = None
                else:
                    curr.next = ListNode(item)
                    curr = curr.next
    def __str__(self):
        res = []
        curr = self
        while curr is not None:
            res.append(curr.val)
            curr = curr.next
        return str(res)

import heapq


class Item:
    def __init__(self, node):
        self.node = node

    def __cmp__(self, other):
        return self.node.val - other.node.val
class Solution(object):

    def add_res(self, item):
        val = item.val
        if self.res is None:
            self.res = ListNode(val)
            self.curr = self.res
        else:
            self.curr.next = ListNode(val)
            self.curr = self.curr.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        把lists中所有第一个元素入堆
        如果堆中还有元素
            弹出最小的一个
            并把弹出的元素指向的下一个元素入堆
            添加到结果中
        """
        if not lists: return None
        self.lists = lists
        k = len(lists)
        if k <= 0: return None
        if k == 1: return lists[0]
        self.res = None
        self.heap = []
        for l in lists:
            if l:
                self.heap.append(Item(l))
        heapq.heapify(self.heap)
        while self.heap:
            item = heapq.heappop(self.heap)
            if item.node.next:
                heapq.heappush(self.heap, Item(item.node.next))
            self.add_res(item.node)
        return self.res




if __name__ == '__main__':
    s = Solution()
    print s.mergeKLists([
        ListNode([1, 4, 5]),
        ListNode([1, 3, 4]),
        ListNode([2, 6]),
    ])