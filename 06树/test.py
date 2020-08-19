from queue import SQueue as queue
# Definition for a Treeary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self, elist=[]):
        self.level_res = []
        self.lst =list(elist)
        self.root = self.build_tree(self.lst)

    def build_tree(self, lst):
        for i in range(len(lst)):
            node = TreeNode(lst[i])
            lst[i] = node

        lg = len(lst)
        for i in range((lg-1)//2, -1, -1):  # 利用完全二叉树的索引关系
            p = lst[i]
            if 2*i+1 < lg:
                p.left = lst[2*i+1]
            if 2*i+2 < lg:
                p.right = lst[2*i+2]
            lst[i] = p
        return lst[0]

    def level_order(self):
        t = self.root
        if t is None:
            return []
        q = queue()
        q.enqueue(t)
        while not q.is_empty():
            temp = q.dequeue()
            if temp.val is not None:  # 可删
                self.level_res.append(temp.val)
            if temp.left is not None:
                q.enqueue(temp.left)
            if temp.right is not None:
                q.enqueue(temp.right)
        return self.level_res
        
        
tree = [0, 1, 2, 3, 4, 5, 6, 7, None, 9]
t = Solution(tree)
print(t.level_order())


# for i in range(len(tree)):
#     p = tree[i]
#     p += 1
#     tree[i] = p
# print(tree)
# def divid(lst):
#     for i in range(len(lst)):
#         node = TreeNode(lst[i])
#         lst[i] = node
#
#     res = []
#     index, l, r = 0, 0, 0
#
#     while True:
#         r = l + pow(2, index)
#         res.append(lst[l:r])
#         index, l = index + 1, r
#         if l >= len(lst):
#             break
#     return res

#################################################################################
class PrioQueueError(ValueError):
    pass

# class PrioQue():
#     def __init__(self, elist):
#         """设置 大优先级高"""
#         self._elements = list(elist)
#         self._len = len(self._elements)
#         if elist:
#             self.buildheap()
#
#     def buildheap(self):
#         end = self._len
#         # 节点end的父节点为end//2-1
#         for i in range(end//2-1, -1, -1):  # 中间的-1取不到，是左闭右开区间
#             self.sift_down(self._elements[i], i, end)
#         print('初始队列：', self._elements)
#
#     def is_empty(self):
#         return self._len == 0
#
#     def enqueue(self, data):
#         # 为第一次交换做准备
#         self._elements.append(None)
#         self._len += 1
#         self.sift_up(data, self._len-1)
#         return
#
#     def sift_up(self, data, last_index):
#         """要插入的元素和队列最后一个位置的索引"""
#         """位置合法 + 数值合适"""
#         base_pos, parent_pos = last_index, (last_index - 1) // 2
#         while parent_pos >= 0 and data > self._elements[parent_pos]:
#             self._elements[base_pos] = self._elements[parent_pos]
#             base_pos, parent_pos = parent_pos, (parent_pos - 1) // 2
#         self._elements[base_pos] = data  # 退出循环后赋值
#         return
#
#     def dequeue(self):
#         if self.is_empty():
#             raise PrioQueueError
#         first = self._elements[0]
#         last = self._elements.pop()
#         self._len -= 1
#         if self._len > 0:
#             self.sift_down(last, 0, self._len)
#         return first
#
#     def sift_down(self, data, begin, end):
#         """begin可以视作根节点，从该处三角下筛"""
#         """下筛的时候就不考虑原根节点了"""
#         base_pos, target = begin, 2 * begin + 1
#         while target < end:  # 确定最小的→交换
#             if target + 1 < end and self._elements[target] < self._elements[1 + target]:  # 第一个条件防止没有右子树
#                 target += 1
#             if data > self._elements[target]:
#                 break  # 是三值中最da的，位置对
#             else:
#                 self._elements[base_pos] = self._elements[target]
#             base_pos, target = target, target * 2 + 1
#         self._elements[base_pos] = data
#         return
#################################################################################
# import re
# err_dict = {}
# res = []
# while True:
#     try:
#         x = input().strip()
#         path, line = re.split(r' +', x)  # 空格分割
#         info = path+' '+line
#         if info not in err_dict:
#             err_dict[info] = 1
#             res.append(info)
#         else:
#             err_dict[info] += 1
#     except:
#         break
#
# if len(res) >8:
#     res = res[-8:]
# for info in res:
#     path, line = info.split(' ')
#     path = re.split(r'\\', path)[-1]
#     if len(path) > 16:
#         path = path[-16:]
#     print(path+' '+line+' '+str(err_dict[info]))



