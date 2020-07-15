def slide_window(nums, s):
    i, j, r = 0, 0, len(nums) + 1
    sums = []         # complexity:O(n) to O(1)
    for num in nums:
        if not sums:  # list is empty
            sums.append(num)
        else:
            sums.append(sums[-1] + num)

    while (i < len(nums)) and (j < len(nums)):
        if sums[j] - sums[i] + nums[i] < s:
            j += 1
        else:
            if j - i + 1 < r:
                r = j - i + 1
            i += 1

    if r != len(nums) + 1:  # 有解
        return r
    else:
        return 0

lst = [2,2,5,6,3,2,7,4,4]

print(slide_window(lst, 0))

# ################# sum版本 #################################
def slide_complex(lst, s):
    l, r, ans= 0, 0, len(lst)  # left-right boundary and answer

    while l < len(lst) and r < len(lst):
        if sum(lst[l:r+1]) < s:  # 如果访问a[1:0]返回为空，sum为0，
            r += 1
        else:  # get possible
            if r - l + 1 < ans:
                ans = r - l + 1
            l += 1
        if l > r:
            r += 1  # 考虑s=0
    if ans < 1 + len(lst):
        return ans
    else:
        return 0

# print(slide_complex([9,8,7,6,5],0))

