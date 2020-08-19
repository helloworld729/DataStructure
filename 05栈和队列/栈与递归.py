# 背包问题
less = False
more = False
info = ""
def knap(weights, wlist):
    n = len(wlist)
    if weights == 0:
        return True
    elif weights > 0 and n == 0:
        global more
        more = True
        return False
    elif weights < 0:
        global less
        less = True
        return False

    if knap(weights, wlist[:-1]):
        return True
    elif knap(weights-wlist[-1], wlist[:-1]):
        global info
        info += str(wlist[-1]) + "-"
        return True
    else:
        return False


if knap(12, [1, 2, 3, 5, 4, 29]):
    print("有解: " + info[: -1])
elif less:
    print("背包太小")
elif more:
    print("背包太大")