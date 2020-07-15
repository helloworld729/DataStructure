def ip_check(ip_str):
    ip_seg = ip_str.strip().split('.')  # 4
    if len(ip_seg) != 4:
        return False
    try:
        ip_seg = [int(i) for i in ip_seg]

        if 1 <= ip_seg[0] <= 126 and 0 <= ip_seg[1] <= 255 and 0 <= ip_seg[2] <= 255 and 0 <= ip_seg[3] <= 255:
            res = 'A'
            if ip_seg[0] == 10 and 0 <= ip_seg[1] <= 255 and 0 <= ip_seg[2] <= 255 and 0 <= ip_seg[3] <= 255:
                res = 'private'

        elif 128 <= ip_seg[0] <= 191 and 0 <= ip_seg[1] <= 255 and 0 <= ip_seg[2] <= 255 and 0 <= ip_seg[3] <= 255:
            res = 'B'
            if ip_seg[0] == 172 and 16 <= ip_seg[1] <= 31 and 0 <= ip_seg[2] <= 255 and 0 <= ip_seg[3] <= 255:
                res = 'private'

        elif 192 <= ip_seg[0] <= 223 and 0 <= ip_seg[1] <= 255 and 0 <= ip_seg[2] <= 255 and 0 <= ip_seg[3] <= 255:
            res = 'C'
            if ip_seg[0] == 192 and ip_seg[1] == 168 and 0 <= ip_seg[2] <= 255 and 0 <= ip_seg[3] <= 255:
                res = 'private'

        elif 224 <= ip_seg[0] <= 239 and 0 <= ip_seg[1] <= 255 and 0 <= ip_seg[2] <= 255 and 0 <= ip_seg[3] <= 255:
            res = 'D'
        elif 240 <= ip_seg[0] <= 255 and 0 <= ip_seg[1] <= 255 and 0 <= ip_seg[2] <= 255 and 0 <= ip_seg[3] <= 255:
            res = 'E'
        elif ip_seg[0] == 0:
            res = 'pass'
        else:
            return False
        return res
    except:
        return False

# print(ip_check('47.191.88.206'))

# ############################# 第K个最小的值 ###############################################
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ]
# import heapq
# def kthSmallest(matrix, k: int) -> int:
#     m, n = len(matrix), len(matrix[0])
#     h = []
#     for i in range(n):
#         heapq.heappush(h, (matrix[0][i], 0, i))  # 值和索引
#     for i in range(k - 1):
#         item = heapq.heappop(h)
#         if item[1] + 1 < m:
#             heapq.heappush(h, (matrix[item[1] + 1][item[2]], item[1] + 1, item[2]))
#     return heapq.heappop(h)[0]
# print(kthSmallest(matrix, 8))

# ############################# 堆 ###############################################
# import heapq
# lst = [1,2,5,7,3,4]
# h = []  # 堆容器
# for i in lst:
#     heapq.heappush(h, i)  # 入堆
# print(heapq.heappop(h))   # 出堆
# print(heapq.nsmallest(2, h))  # 最大的前n个数（不推荐）
# print(heapq.nlargest(2, h))   # 最小的前n个数
#
# # 第二种方式
# heapq.heapify(lst)  # list堆化
# print(heapq.heappop(lst))
# print(heapq.nsmallest(2, lst))
# print(heapq.nlargest(2, lst))

# ############################# 队列 ###############################################
# from queue import Queue
# que = Queue()
# for i in range(3):
#     que.put(i)  # 入队
# print(que.queue)
#
# for i in range(3):
#     print(que.get(), end=' ')  # 出队并返回结果
# print('\n',que.queue)

from collections import deque
# 默认在右侧压入和弹出
dequeQueue = deque(['b', 'c', 'd'])
print(dequeQueue)
dequeQueue.append('e')    # 默认在右侧插入新元素
dequeQueue.appendleft('a')  #在左侧插入新元素
print(dequeQueue)
dequeQueue.rotate(2)    #循环右移2次
print('循环右移2次后的队列',dequeQueue)
dequeQueue.popleft()    #返回并删除队列最左端元素
print('删除最左端元素后的队列：',dequeQueue)
dequeQueue.pop()    #返回并删除队列最右端元素
print('删除最右端元素后的队列：',dequeQueue)