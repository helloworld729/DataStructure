class Solution:
    def isBipartite(self, graph) -> bool:
        count = 0
        vnum = len(graph)
        visited = [-1] * vnum  # 访问列表

        for index, edges in enumerate(graph):
            if edges:
                color = 0
                st = [(0, graph[index], 1 - color)]  # 栈初始化
                visited[index] = color
                count += 1
                print('初始化节点{},分配的颜色{}'.format(index, color))
                break

        if index == vnum - 1:
            return True

        while st:
            print('new')
            print(st)
            index, edegs, color = st.pop()
            if index < len(edegs):
                v = edegs[index]  # 当前的点
                print('当前访问的节点{},分配的颜色{}'.format(v, color))
                st.append((index + 1, edegs, color))  # 同一边表，颜色不变

                if visited[v] == -1:  # 未被访问
                    count += 1
                    print('当前count',count)
                    visited[v] = color  # 分配的颜色
                    st.append((0, graph[v], 1 - color))
                elif visited[v] != color:
                    print('current code', v)
                    print('memorory', visited[v])
                    print('get value', color)
                    return False
            if not st and count < vnum:
                for i in range(len(visited)):
                    if visited[i] == -1:
                        if graph[i]:
                            color = 0
                            st = [(0, graph[index], 1 - color)]  # 栈初始化
                            visited[index] = color
                            count += 1
                            break
        return True

a = Solution()
print(a.isBipartite(graph=[[1],[0],[4],[4],[2,3]]))
