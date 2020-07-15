def merge(lfrom, lto, low, mid, high):
    i, j, k = low, mid, low
    while i < mid and j < high:
        """循环跳出条件为某段完毕"""
        if lfrom[i] >= lfrom[j]:  # 大值上岸
            lto[k] = lfrom[i]
            i += 1
        else:
            lto[k] = lfrom[j]
            j += 1
        k += 1  # 关键
    while i < mid:
        lto[k] = lfrom[i]
        i += 1
        k += 1
    while j < high:
        lto[k] = lfrom[j]
        k += 1
        j += 1
    return lto

# lfrom = [2, 3, 4] + [5, 7, 1]
# lto = [None] * 6
# print(merge(lfrom, lto, 0, 3, len(lfrom)))

def boundary_set(lfrom, lto, llen, slen):
    pos = 0
    while pos + 2*slen <= llen:  # 注意等于号
        print("逐鹿中原")
        merge(lfrom, lto, pos, pos + slen, pos + 2 * slen)
        pos += 2 * slen

    if pos+ slen < llen:  # 剩下两段
        print("岂曰无衣")
        merge(lfrom, lto, pos, pos+slen, llen)
    else:
        while pos < llen:  # 剩下一段
            print("与子同袍")
            lto[pos] = lfrom[pos]
            pos += 1
    return lto
# lfrom = [7,4,5,2]
# lto = [None] * len(lfrom)
# print(boundary_set(lfrom, lto, len(lfrom), 2))

def mer_con(lst):
    slen, llen = 1, len(lst)
    templst = [None] * llen

    while slen < llen:
        boundary_set(lst, templst, llen, slen)
        slen *= 2
        boundary_set(templst, lst, llen, slen)
        slen *= 2
    return lst

# print(mer_con([10, 8,9,5,2,1,4,56,23,7,8]))

def funa(x):
    print(id(x))
    x += 1
    print(id(x))

def funb(a):
    a += 1
    # funa(a)

a = 10
funb(a)
print(a)
