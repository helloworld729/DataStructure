from node与指针测试 import LNode as Node

class LinkedListUnderflow(ValueError):
    pass


class LCList():  # 注意空表和长度为1的表
    def __init__(self):
        """循环单链表"""
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):  # 前端增加
        node = Node(elem)
        if self._rear is None:
            node._next = node  # 指向自身
            self._rear = node
        else:
            node._next = self._rear._next
            self._rear._next = node

    def append(self, elem):  # 后端增加
        """有意思"""
        self.prepend(elem)
        self._rear = self._rear._next

    def pop(self):  # 前端删除
        if self._rear is None:
            raise LinkedListUnderflow
        elif self._rear == self._rear._next:
            self._rear = None
        else:
            self._rear._next = self._rear._next._next

    def pop_last(self):
        if self._rear is None:
            raise LinkedListUnderflow
        elif self._rear == self._rear._next:
            self._rear = None
        else:
            p = self._rear._next
            while p is not self._rear:
                if p._next == self._rear:
                    self._rear = p
                    self.pop() # 执行一次前端删除
                    break
                p = p._next

    def elements(self):
        p = self._rear._next
        while p is not self._rear:
            yield p._elem
            p = p._next


lclist = LCList()
for i in range(1, 6):
    lclist.append(i)
for ele in lclist.elements():
    print(ele, end=' ')
print('')

lclist.prepend(0)
lclist.append(5)
for ele in lclist.elements():
    print(ele, end=' ')
print('')

lclist.pop()
lclist.pop_last()
for ele in lclist.elements():
    print(ele, end=' ')


