from queue import SQueue as queue
from list_stack import Stack as stack

class BinTNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def count_BinTNode(t):
    if t is None:
        return 0
    else:
        total = 1 + count_BinTNode(t.left) + count_BinTNode(t.right)
    return total

total = 0
def count_BinTNode2(t):
    if t is None:  # 边界条件
        return
    else:
        global total
        total += 1
        count_BinTNode2(t.left)
        count_BinTNode2(t.right)

def sum_BinTNode(t):
    if t is None:
        return 0
    else:
        return t.data + sum_BinTNode(t.letf) + sum_BinTNode(t.right)

def pre_order(root, lst=[]):
    if root is None:  # 边界条件
        return
    lst.append(root.data)  # 处理方法
    pre_order(root.left)   # 递归推进
    pre_order(root.right)  # 递归推进
    return lst

def mid_order(t, op):
    if t is None:
        return
    mid_order(t.left, op)  # 处理左子树
    op(t.data, end=' ')  # 处理自己
    mid_order(t.right, op)  # 处理右子树
    return

def last_order(t, op):
    if t is None:
        return
    last_order(t.left, op)
    last_order(t.right, op)
    op(t.data, end=' ')
    return

def level_order(t, op):
    if t is None:
        return
    q = queue()
    q.enqueue(t)
    while not q.is_empty():
        temp = q.dequeue()
        op(temp.data, end=' ')
        if temp.left is not None:
            q.enqueue(temp.left)
        if temp.right is not None:
            q.enqueue(temp.right)
    return

def preorder_elements(t):
    s= stack()
    s.push(t)
    while not s.is_empty():
        t = s.pop()
        while t is not None:
            yield t.data
            s.push(t.right)
            t = t.left

def preorder_nonrec(root):
    res, st = [], []
    st.append(root)

    while st:  # 续右
        node = st.pop()
        while node is not None:  # 左下且读
            res.append(node.data)
            st.append(node.right)
            node = node.left
    return res

def midorder_nonrec(root):
    res, st = [], []
    while st or root is not None:
        while root is not None:  # 左下
            st.append(root)  # 一定不会压入None
            root = root.left
        node = st.pop()

        res.append(node.data)
        root = node.right
    return res

def postorder_nonrec(root):
    res, st = [], []
    while st or root is not None:
        """判root只在第一次有用，为什么不在外层压入root？因为子循环还要压入root"""
        while root is not None:  # 见左捣底
            st.append(root)
            root = root.left if root.left is not None else root.right  # 只要后继在前驱之前就行

        node = st.pop()
        res.append(node.data)

        if st and st[-1].left == node:  # 求-1必须先判空
            """判空的原因：防止-1越界"""
            """判左的原因：不判左的话某个右节点反复弹出压入"""
            root = st[-1].right
        else:
            root = None
    return res

root = BinTNode(0, BinTNode(1, BinTNode(3, BinTNode(7), BinTNode(8)),
                BinTNode(4, BinTNode(9), None)), BinTNode(2, BinTNode(5),
                BinTNode(6)))

print('深度优先：', end='')
level_order(root, print)
print('')
print('先序遍历：', end='')
print(pre_order(root))
print('')
print('先序遍历：', end='')
print(preorder_nonrec(root))
print('')
print('中序遍历：', end='')
mid_order(root, print)
print('')
print('中序遍历：', end='')
print(midorder_nonrec(root))
print('')
print('后序遍历：', end='')
last_order(root, print)
print('')
print('后序遍历：', end='')
print(postorder_nonrec(root))
print('')
