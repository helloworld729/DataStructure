class PrioQueueError(ValueError):
    pass

class PrioQue():
    def __init__(self, elist):
        """栈尾优先级最高"""
        # 拷贝防共享
        self._elements = list(elist)
        self._elements.sort(reverse=True)
        # 采用静态长度，注意维护
        self._len = len(self._elements)

    def is_empty(self):
        return self._len == 0

    def enqueue(self, data):
        """要为两种情况设定默认位置"""
        pos = self._len  # 长度为0或者插入值最小
        for i in range(self._len):  # 定位
            if self._elements[i] < data:
                pos = i
                break
        self._elements.insert(pos, data)
        self._len += 1
        return

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in dequeue")
        e = self._elements[-1]
        self._elements.pop()
        return e

    def content(self):
        print(self._elements)


pq = PrioQue([])
s = [12, 4, 7, 8, 3, 5, 6, 4]
for data in s:
    pq.enqueue(data)
    pq.content()
