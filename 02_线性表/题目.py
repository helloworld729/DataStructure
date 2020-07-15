"""
题目描述
给定一个单链表的头部节点 head，链表长度为 N，如果 N 是偶数，
那么前 N / 2 个节点算作左半区，后 N / 2 个节点算作右半区；
如果 N 为奇数，那么前 N / 2 个节点算作左半区，后 N / 2 + 1
个节点算作右半区。左半区从左到右依次记为 L1->L2->...，右半区
从左到右依次记为 R1->R2->...，请将单链表调整成 L1->R1->L2->R2->... 的形式。
"""
class NODE():
    def __init__(self, elem):
        self._next = None
        self._elem = elem


class LLIST():
    def __init__(self):
        self._head = None
        self._len = 0

    def append(self, elem):
        self._len += 1
        node = NODE(elem)
        if self._head is None:
            self._head = node
        else:
            p = self._head
            while p._next is not None:
                p = p._next
            p._next = node

    def for_each(self, op):
        p = self._head
        while p is not None:
            op(p._elem, end=' ')
            p = p._next

    def pop_last(self):
        p = self._head
        if self._head is None:
            raise ValueError
        elif self._head._next is None:
            self._head = None
        else:
            while p._next._next is not None:
                p = p._next
            p._next = None

    def mix(self):
        p = self._head
        for i in range(self._len // 2):
            p = p._next
        right = p
        temp_right = right

        p = self._head

        while p._next is not right:
            node = NODE(elem=temp_right._elem)
            node._next = p._next
            p._next = node
            p = p._next._next
            temp_right = temp_right._next

        if temp_right is not None:
            node = NODE(temp_right._elem)
            p._next = temp_right

llist = LLIST()
for i  in range(1,6):
    llist.append(i)
llist.mix()
llist.for_each(print)