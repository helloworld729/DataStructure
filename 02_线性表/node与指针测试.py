class LNode():
    """链表结点类"""
    def __init__(self, elem, next=None):
        self._elem = elem
        self._next = next

#
# llist = LNode(1)
# p = llist  # head
#
# for i in range(2, 6):
#     node = LNode(elem=i)  # 创建变量
#     p._next = node        # 别名指针
#     p = node
#
# p = llist
# while p:
#     print('结点位置{}  结点长度{}  结点内容{}'.format(id(p), p.__sizeof__(), p._elem))
#     p = p._next
