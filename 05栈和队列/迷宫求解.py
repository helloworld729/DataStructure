maze = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],

]
start = (0, 0)
end = (3, 5)
dirs = [
    [1,  0],  # 下
    [0,  1],  # 右
    [-1, 0],  # 左
    [0, -1],  # 上
]

def mark(maze, pos):
    """已经访问的位置标记"""
    maze[pos[0]][pos[1]] = 2

def possible(maze, pos):
    """pos是否可以访问"""
    flag = False
    if pos[0] >=0 and pos[1] >=0 :
        try:
            if maze[pos[0]][pos[1]] == 0:
                flag = True
                return flag
        except:pass
    return flag

def find_path(maze, pos, end):
    # print("hello", end=' ')
    # print(pos)
    mark(maze, pos)
    if pos == end:
        print(pos, end=' ')
        return True
    else:
        for i in range(4):
            n_pos = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
            if possible(maze, n_pos):
                if find_path(maze, n_pos, end):
                    print(pos, end=' ')
                    return True   # 提前终结
        return False

find_path(maze, start, end)
print("")
for ele in maze:
    print(ele)


