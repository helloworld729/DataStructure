from list_stack import Stack as stack
# 回溯：返回到局部根节点
# #######################################################
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
    maze[pos[0]][pos[1]] = 2

def possible(maze, pos):
    flag = False
    if pos[0] >=0 and pos[1] >=0 :
        try:
            if maze[pos[0]][pos[1]] == 0:
                flag = True
                return flag
        except:pass
    return flag
# #######################################################


def print_path(end, st):
    print(end, end="")
    for ele in st.elements():
        print('←', ele[0], end="")

def maze_solver(maze, start, end):
    if start == end:
        print(start)
        return
    st = stack()
    mark(maze, start)
    st.push((start, 0))
    while not st.is_empty():  # 重要
        pos, poss_dir = st.pop()
        for i in range(poss_dir, 4):
            next_p = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
            if next_p == end:
                mark(maze, next_p)
                st.push((pos, poss_dir-1))
                print_path(end, st)
                return
            if possible(maze, next_p):
                st.push((pos, i+1))  # 局部根节点
                mark(maze, next_p)
                st.push((next_p, 0))  # 新节点
                break
    print("No path found.")

maze_solver(maze, start, end)
print("")
for row in maze:
    print(row)