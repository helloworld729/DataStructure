class PrioQueueError(ValueError):
    pass

class PrioQue():
    def __init__(self, elist):
        """设置小优先级高"""
        self._elements = list(elist)
        self._len = len(self._elements)
        if elist:
            self.buildheap()

    def buildheap(self):
        end = self._len
        # 节点end的父节点为end//2-1
        for i in range(end//2-1, -1, -1):  # 中间的-1取不到，是左闭右开区间
            self.sift_down(self._elements[i], i, end)
        print('初始队列：', self._elements)

    def is_empty(self):
        return self._len == 0

    def enqueue(self, data):
        # 为第一次交换做准备
        self._elements.append(None)
        self._len += 1
        self.sift_up(data, self._len-1)
        return

    def sift_up(self, data, last_index):
        """要插入的元素和队列最后一个位置的索引"""
        """位置合法 + 数值合适"""
        base_pos, parent_pos = last_index, (last_index - 1) // 2
        while parent_pos >= 0 and data < self._elements[parent_pos]:
            self._elements[base_pos] = self._elements[parent_pos]
            base_pos, parent_pos = parent_pos, (parent_pos - 1) // 2
        self._elements[base_pos] = data  # 退出循环后赋值
        return

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError
        first = self._elements[0]
        last = self._elements.pop()
        self._len -= 1
        if self._len > 0:
            self.sift_down(last, 0, self._len)
        return first

    def sift_down(self, data, begin, end):
        """begin可以视作根节点，从该处三角下筛"""
        """下筛的时候就不考虑原根节点了"""
        base_pos, target = begin, 2 * begin + 1
        while target < end:  # 确定最小的→交换
            if target + 1 < end and self._elements[target] > self._elements[1 + target]:  # 第一个条件防止没有右子树
                target += 1
            if data < self._elements[target]:
                break  # 是三值中最小的，位置对
            else:
                self._elements[base_pos] = self._elements[target]
            base_pos, target = target, target * 2 + 1
        self._elements[base_pos] = data
        return

    def order(self):
        temp = [0]*self._len
        for i in range(self._len):
            temp[i] = self.dequeue()
        return temp

    def content(self):
        print(self._elements)

pq = PrioQue([5, 6, 9, 2, 4, 7])
pq.enqueue(10)
print("队列加10:  ", end='')
pq.content()
pq.dequeue()
print("dequeue后: ", end='')
pq.content()
print("排序后:    ", end='')
print(pq.order())

