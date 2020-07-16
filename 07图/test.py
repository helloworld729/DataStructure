class GraphError(ValueError):
    pass
class Graph():
    def __init__(self, mat, unconn=0):
        self._vnum = len(mat)
        for row in mat:
            if len(row) != self._vnum:
                raise GraphError
        self._mat = mat
        self._unconn = unconn

    def vertex_num(self):
        return self._vnum

    def is_not_valid(self, v):
        return v < 0 or v >= self._vnum

    def add_vertex(self):
        raise GraphError("not support now")

    def add_edge(self, vi, vj, val=1):  # 增
        if self.is_not_valid(vi) or self.is_not_valid(vj):
            raise GraphError("vi or vj is not valid")
        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):  # 查
        if self.is_not_valid(vi) or self.is_not_valid(vj):
            raise GraphError("vi or vj is not valid")
        return self._mat[vi][vj]

    def out_edges(self, vi):  # 返回节点对应的边信息
        if self.is_not_valid(vi):
            raise GraphError("vi is not valid")
        return self._out_edges(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn=0):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges


class GrapgAL(Graph):
    def __init__(self, mat, unconn=0):
        vnum = len(mat)
        for row in mat:
            if len(row) != vnum:
                raise GraphError("不是方阵")
        self._mat = [self._out_edges(mat[i], 0) for i in range(vnum)]  # 二维列表，不是矩阵
        self._vnum = vnum
        self._unconn = unconn

    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1

    def add_edge(self, vi, vj, val=1):
        if self.is_not_valid(vi) or self.is_not_valid(vj):
            raise GraphError("节点非法")
        row = self._mat[vi]
        i = 0
        while i < len(row):
            if vj == row[i][0]:
                self._mat[vi][i] = (vj, val)  # i 是邻接边的在边表索引，不是邻接点的序号
                return
            # if vj < i:  # TODO
            #     break
            if vj < row[i][0]:
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))

    def get_edge(self, vi, vj):
        """获取两个节点之间边信息"""
        if self.is_not_valid(vi) or self.is_not_valid(vj):
            raise GraphError("invalid")
        for con_info in self._mat[vi]:
            if con_info[0] == vj:
                return con_info[1]
        return self._unconn

    def out_edges(self, vi):
        """返回能结点的所有关联边"""
        if self.is_not_valid(vi):
            raise GraphError("结点非法")
        return self._mat[vi]

    def DFS_recur(self, v):
        """基于递归的深度优先"""
        visited = []
        def dfs(v):
            if v not in visited:  # 当前点
                visited.append(v)
            edges = self.out_edges(v)
            edges = [edge[0] for edge in edges]
            diff = [j for j in edges if j not in visited]
            if len(diff) == 0:
                return
            for next_v in diff:  # 邻接点
                dfs(next_v)
        dfs(v)
        return visited

    def DFS_graph(self, v0):
        """非递归思路：压栈的是（访问索引，边表）"""
        visited = [v0]
        edges = self.out_edges(v0)
        st = []
        st.append((0, edges))
        while st:
            i, edges_lst = st.pop()
            st.append((i + 1, edges_lst)) if i + 1 <= len(edges_lst) - 1 else None
            vi = edges_lst[i][0]
            if vi not in visited:
                visited.append(vi)
                st.append((0, self.out_edges(vi)))
        return visited

    def DFS_forest(self):
        """深度遍历生成树"""
        forest = [(0,0)]
        visited = [0]
        def dfs(v):
            edges = self.out_edges(v)
            v_lst = [edge[0] for edge in edges]
            diff = [i for i in v_lst if i not in visited]
            if len(diff) == 0: return
            for vj in diff:
                # 为什么需要再次判断？(注意递归的现场保护)
                # 因为深度推进的过程中，vj可能已经被访问，再回退到vj就多余了。
                if vj not in visited:
                    forest.append((v, vj))
                    visited.append(vj)
                    dfs(vj)
        dfs(0)
        forest.sort(key=lambda x: x[1])
        return forest

    def kruskal(self):  # 最小生成树算法
        """边表统计--优先队列--mst"""
        """停止条件：边够了"""
        mst, edges = [], []
        rep = [i for i in range(self._vnum)]  # 初始化代表元为自己
        for vi in range(self._vnum):  # 边表统计
            vj = self.out_edges(vi)
            for index, weight in vj:
                edges.append((weight, vi, index))
        edges.sort()  # 优先队列

        for weight, vi, vj in edges:
            if rep[vi] != rep[vj]:
                mst.append(((vi, vj), weight))
            if len(mst) == self._vnum - 1:
                break
            srep, trep = rep[vi], rep[vj]
            for i in range(len(rep)):
                if rep[i] == srep:
                    rep[i] = trep
        return mst

    def prim(self):
        """根据地--边表扩展--优先队列"""
        """停止条件：节点够了"""
        mst = [None for i in range(self._vnum)]  # 树枝初始化
        cans = [(0, 0, 0)]  # 候选边初始化
        count = 0  # 连通区初始化
        while count < self._vnum:
            weight, vi, vj = cans.pop()
            if mst[vj]: continue  # 已经在连通区

            count += 1  # 扩展根据地
            mst[vj] = ((vi, vj), weight)
            for vk, vk_weight in self.out_edges(vj):
                cans.append((vk_weight, vj, vk))
            cans.sort(reverse=True)  # 为什么要倒排呢，因为pop从栈尾弹出
        mst.sort()  # 为了print容易观察
        return mst


mat = [
    [0, 10, 1, 0, 1, 0],  # 1 2 4
    [10, 0, 0, 1, 1, 0],  # 0 3 4
    [1, 0, 0, 0, 1, 1],  # 0 4 5
    [0, 1, 0, 0, 0, 0],  # 1
    [1, 1, 1, 0, 0, 0],  # 0 1 2
    [0, 0, 1, 0, 0, 0],  # 2
]
graph = GrapgAL(mat)
print(graph.prim())

