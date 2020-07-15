def merge(lfrom, lto, low, mid, high):
    """
    借助同样大小的空间进行 底层归并
    :param lfrom: 源段 列表
    :param lto: 目标段 列表
    :param low: 左边界（左段可取到）
    :param mid: 中间（右段可取到）
    :param high: 右边界（取不到）
    :return:
    """
    i, j, k = low, mid, low
    while i < mid and j < high:
        if lfrom[i] < lfrom[j]:
            lto[k] = lfrom[i]
            i += 1
        else:
            lto[k] = lfrom[j]
            j += 1
        k += 1

    while i < mid:
        lto[k] = lfrom[i]
        i += 1
        k += 1

    while j < high:
        lto[k] = lfrom[j]
        j += 1
        k += 1

def boundary_set(lfrom, lto, llen, slen):
    """

    :param lfrom:
    :param lto:
    :param llen:总长
    :param slen: 段长
    :return:
    """
    i = 0
    while i + 2 * slen < llen:  # 逐两段归并(逐鹿中原)
        merge(lfrom, lto, i, i + slen, i + 2 * slen)
        i += 2 * slen
    if i + slen < llen:  # 剩下两段 后段长度小于slen(岂曰无衣)
        merge(lfrom, lto, i, i + slen, llen)
    else:                # 只剩下一段
        for j in range(i, llen):  # (孤芳自赏)
            lto[j] = lfrom[j]

def merge_sort(lst):
    slen, llen = 1, len(lst)
    templst = [None] * llen
    while slen < llen:
        boundary_set(lst, templst, llen, slen)
        print(templst)
        slen *= 2
        boundary_set(templst, lst, llen, slen)  # 如果在templst中完毕，此处会直接复制回来
        print(templst)
        slen *= 2
    return lst

print(merge_sort([56,8,7,9,6,5,3,2,1]))

print("=========================== 分割线 =======================================")

"""
转换控制(列表角色、段长)
划分区间:
归并排序
"""

def funb(a):
    a[0] += 1

a = [1, 2]
print(a)
funb(a)
print(a)