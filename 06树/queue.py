class QueueError(ValueError):
    pass


class SQueue():
    def __init__(self, init_len=8):
        self._len = init_len           # 长度
        self._elems = [0] * self._len  # 数据存储区
        self._head = 0                 # index
        self._num = 0                  # 元素个数

    def is_empty(self):
        return self._num == 0

    def peek(self):
        if self._num == 0:
            raise QueueError
        else:
            return self._elems[self._head]  # 返回表头

    def dequeue(self):
        if self._num == 0:
            raise QueueError
        else:
            e = self._elems[self._head]
            self._head = (self._head + 1) % self._len
            self._num -= 1
            return e

    def enqueue(self, e):
        if self._len == self._num:
            self.extend()
        self._elems[(self._head + self._num) % self._len] = e
        self._num += 1

    def extend(self):
        """按照原队列的正确顺序入栈"""
        print("执行扩展函数")
        old_len = self._len  # 长度约束
        self._len *= 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[self._head + i % old_len]
        self._elems, self._head = new_elems, 0

# q = SQueue(init_len=5)

# for i in range(1, 10):
#     q.enqueue(None)
# for i in range(9):
#     print(q.dequeue(), end=" ")
