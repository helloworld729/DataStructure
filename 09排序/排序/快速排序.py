def q_sort0(lst, l, r):
    """
    快速排序
    :param lst:待排列表
    :param l: 左指针
    :param r: 右指针
    :return:
    """
    if l >= r:  # 边界条件，只有一个元素
        return

    i, j = l, r  # l和r要控制递归
    pivot = lst[i]  # 选取第一个元素作为pivot

    while i < j:    # 处理办法：partition
        while i < j and lst[j] >= pivot:  # 比基准大则左滑，小则停止
            j -= 1
        if i < j:  # 查距填坑
            lst[i] = lst[j]
            i += 1
        while i < j and lst[i] <= pivot:  # 比基准小则右滑，大则停止
            i += 1
        if i < j:  # 查距填坑
            lst[j] = lst[i]
            j -= 1
    lst[i] = pivot  # 跳出循环后i==j，为pivot的正确位置

    q_sort0(lst, l, i-1)  # 递归推进，左侧快排，因为lst改变所以递归推进放到后面
    q_sort0(lst, i+1, r)  # 递归推进，右侧快排，

    return lst


def q_sort(lst, l, r, k):
    """
    快速排序
    :param lst:待排列表
    :param l: 左指针
    :param r: 右指针
    :param k: 返回第K大的元素，如果pivot位置在k右边，那么右边的部分不用继续排序
    :return:
    """
    if k <= 0:
        return None
    # l, r = 0, len(lst) - 1
    if l >= r:  # 边界条件，只有一个元素
        return lst[l]

    i, j = l, r  # l和r要控制递归
    pivot = lst[i]  # 选取第一个元素作为pivot

    while i < j:  # 处理办法：partition
        while i < j and lst[j] >= pivot:  # 比基准大则左滑，小则停止, 第一个条件保证第一个数最小时数组不会越界
            j -= 1
        if i < j:  # 查距填坑
            lst[i] = lst[j]
            i += 1
        while i < j and lst[i] <= pivot:  # 比基准小则右滑，大则停止
            i += 1
        if i < j:  # 查距填坑
            lst[j] = lst[i]
            j -= 1
    lst[i] = pivot  # 跳出循环后i==j，为pivot的正确位置

    if i == k - 1:
        return lst[i]
    elif i < k - 1:
        return q_sort(lst, i+1, r, k)  # 递归推进，右侧快排，由于i和k都是全局的所以k不变
    elif i > k - 1:
        return q_sort(lst, l, i-1, k)  # 递归推进，左侧快排，因为lst改变所以递归推进放到后面

def q_reverse(lst, l, r):
    if l >= r:
        return
    # print(id(lst))
    i, j = l, r
    pivot = lst[i]
    while i < j:
        while i < j and lst[j] <= pivot:
            j -= 1
        if i < j:
            lst[i] = lst[j]
            i += 1

        while i < j and lst[i] >= pivot:
            i += 1
        if i < j:
            lst[j] = lst[i]

    lst[i] = pivot
    q_reverse(lst, l, i - 1)  # 重要
    q_reverse(lst, i+1, r)  # 重要
    return lst

def q_reverse2(lst, l, r):
    if len(lst) <= 1:
        return lst
    i, j = l, r
    print(id(lst))
    pivot = lst[i]
    while i < j:
        while i < j and lst[j] <= pivot:
            j -= 1
        if i < j:
            lst[i] = lst[j]
            i += 1

        while i < j and lst[i] >= pivot:
            i += 1
        if i < j:
            lst[j] = lst[i]

    lst[i] = pivot
    ll = q_reverse2(lst[0: i], 0, i - 1)  # 重要
    lr = q_reverse2(lst[i+1:], 0, r-i-1)  # 重要
    return ll + [pivot] + lr


a = [3,4,6,5]
for i in range(1, len(a)+1):
    result = q_sort(a,l=0,r=len(a)-1,k=i)
    print(result)

"""
反向遍历的两种方法：
1、在向下递归的过程中，控制区间, 变量始终是一个变量,例如：
id:1030174604168
id:1030174604168
id:1030174604168
id:1030174604168
id:1030174604168
id:1030174604168
[100, 89, 78, 56, 56, 45, 45, 23, 12, 12]

2、在向下递归的过程中，列表切片, 但是这样相当于创建了一个新的变量
412138929032
412138770824
412138881288
412136800584
412138881288
412138881224
[100, 89, 78, 56, 56, 45, 45, 23, 12, 12]

应该采用第一种方法较好

思路快速建立，以倒排为例：
1、右边的数字应该小，所以若当前指向较小(合理)则左滑，遇到大于pivot的值停下 ->合理左滑，否则停下
2、如果距离合适，把数据抛到对面的坑  -> 查距填坑
"""