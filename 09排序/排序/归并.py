def merge(lst, left, middle, right):
    """ 借助两个辅助数组，将原数组归并 """
    l_len, r_len = middle-left+1, right-middle  # 辅助数组长度
    l = lst[left: middle+1]
    r = lst[middle+1: right+1]  # 注意右边界
    i, j = 0, 0
    k = left
    while i <= l_len-1 and j <= r_len-1:
        if l[i] < r[j]:
            lst[k] = l[i]
            i += 1
        else:
            lst[k] = r[j]
            j += 1
        k += 1

    if i <= l_len-1:
        lst[k:right+1] = l[i:l_len]

    if j <= r_len-1:
        lst[k: right+1] = r[j:r_len]

def mergesort(lst, left, right):  # 闭区间
    """  对列表lst的left-->right区间排序，方法是：先将两个子区间分别排序，然后22合并 """
    if left >= right: return
    middle = left + (right-left)//2
    mergesort(lst, left, middle)
    mergesort(lst, middle+1, right)  # 参数个数
    merge(lst, left, middle, right)

lst = [1, 2, 4, 3, 6, 5, 8, 7, 0]
mergesort(lst, 0, len(lst)-1)
print(lst)
