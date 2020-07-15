from queue import SQueue as queue
from list_stack import Stack as stack

class BinTNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinTree():
    def __init__(self):
        self._root = None

    def set_root(self, root):
        self._root = root

    def pre_order(self, op):
        s = stack()
        s.push(self._root)
        while not s.is_empty():  # 非空栈
            t = s.pop()
            while t is not None:
                op(t.data, end=' ')
                s.push(t.right)
                t = t.left

    def level_order(self, op):
        if self._root is None:
            return
        q = queue()
        q.enqueue(self._root)
        while not q.is_empty():
            temp = q.dequeue()
            op(temp.data, end=' ')
            if temp.left is not None:
                q.enqueue(temp.left)
            if temp.right is not None:
                q.enqueue(temp.right)
        return


root = BinTNode(0, BinTNode(1, BinTNode(3, BinTNode(7), BinTNode(8)),
                BinTNode(4, BinTNode(9), None)), BinTNode(2, BinTNode(5),
                BinTNode(6)))

tree = BinTree()
tree.set_root(root)
tree.level_order(print)
print()
tree.pre_order(print)
