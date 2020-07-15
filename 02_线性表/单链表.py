from node与指针测试 import LNode as Node

class LinkedListUnderflow(ValueError):
    pass

class LLIST():
    def __init__(self):
        """单链表"""
        self._head = None
        self._len = 0

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        node = Node(elem, self._head)  # 挂靠
        self._head = node              # 换头
        self._len += 1

    def append(self, elem):
        node = Node(elem)
        p = self._head
        if self._head is None:  # 空表
            self._head = node   # 以下等价
            # self.prepend(elem)
            return
        while p._next is not None:  # 摸底
            p = p._next
        p._next = node  # 链接

    def pop(self):  # 弹出头部
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        # 先拷贝再去头
        e = self._head._elem
        self._head = self._head._next
        self._len -= 1
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("IN POP_LAST")
        if self._head._next is None:  # 长度为1
            e = self._head._elem
            self._head = None
            return e
        p = self._head
        while p._next._next is not None:
            p = p._next
        e = p._next._elem
        p._next = None
        return e

    def for_each(self, op):
        p = self._head
        while p is not None:
            p._elem = op(p._elem)
            p = p._next

    def elements(self):
        p = self._head
        while p is not None:
            yield p._elem
            p = p._next

    def find_elems(self, op):
        p = self._head
        while p is not None:
            if op(p._elem):
                yield p._elem
            p = p._next

    def print_all(self):
        infos = ''
        for info in self.elements():
            infos += info + '->'
        infos = infos[:-2]
        print(infos)

    def reverse(self):
        already = None  # 初始化反转后的最后一个元素
        while self._head is not None:
            p = self._head  # 当前节点.此时p就是指针
            self._head = p._next  # 头部后移，为下一次反指做准备
            p._next = already  # 链接到已经反转好的部分
            already = p
        self._head = already


llist = LLIST()
llist.append("1")
llist.append("加工")
llist.append("2")
llist.append("销售")

# for i in range(1, 4):
#     llist.append(i)
#
# llist.for_each(lambda x: 1 + x)


llist.print_all()
llist.reverse()
llist.print_all()