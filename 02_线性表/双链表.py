class DLNODE():
    def __init__(self, elem, prev=None, next=None):
        """双链表"""
        self._prev = prev
        self._next = next
        self._elem = elem


class DLnodeFlow(ValueError):
    pass


class DLLIST():
    def __init__(self):
        """双链表"""
        self._head = None
        self._rear = None

    def prepend(self, elem):  # 头结点的prev是None，尾结点的next是None
        node = DLNODE(elem, next=self._head,)  # 直连头结点
        if self._head is None:  #
            self._rear = node
        else:
            self._head._prev = node
        self._head = node  # 注意这里

    def append(self, elem):
        node = DLNODE(elem, prev=self._rear)
        if self._head is None:
            self._head = node
        else:
            self._rear._next = node
        self._rear = node  # 注意这里

    def elements(self):
        p = self._head
        while p is not None:
            yield p._elem
            p = p._next

    def re_elements(self):
        p = self._rear
        while p is not None:
            yield p._elem
            p = p._prev

dllist = DLLIST()
for i in range(1, 5):
    dllist.append(i)
for elem in dllist.elements():
    print(elem, end=' ')
print('')
dllist.prepend(0)
for elem in dllist.re_elements():
    print(elem, end=' ')







