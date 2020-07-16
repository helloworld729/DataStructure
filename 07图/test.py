class GraphError(ValueError):
    pass


class Graph():
    def __init__(self, mat, unconn=0):
        vnum = len(mat)  # 节点数目
        for x in mat:
            if len(x) != vnum:
                raise ValueError("Arguments for Graph.")
        self._mat = mat
        self._unconn = unconn
        self._vnum = vnum

    def vertex_num(self):
        """结点数目"""
        return self._vnum

    def is_invalid(self, v):
        """合法性检查"""
        #         print(v, self._vnum)
        return v < 0 or v >= self._vnum

    def add_vertex(self):
        """增加结点"""
        raise GraphError("not support...")

    def add_edge(self, vi, vj, val=1):
        """创建边"""
        if self.is_invalid(vi) or self.is_invalid(vj):
            raise GraphError('vi or vj is invalid')
        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):
        """根据索引获取边的信息"""
        if self.is_invalid(vi) or self.is_invalid(vj):
            raise GraphError('vi or vj is invalid')
        return self._mat[vi][vj]

    def __str__(self):
        return "[\n" + ",\n".join(map(str, self._mat)) + "\n]" + "\nunconn: " + str(self._unconn)

    def out_edges(self, vi):
        """返回某个节点对应的边的信息"""
        if self.is_invalid(vi):
            raise GraphError('vi or vj is invalid')
        return self._out_edges(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn=0):  # 返回节点的有效边列表
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges


class GraphAL(Graph):
    def __init__(self, mat=[], unconn=0):
        vnum = len(mat)
        for row in mat:
            if len(row) != vnum:
                raise GraphError('初始化不是方阵')
        # 不是矩阵，是列表嵌套
        self._mat = [self._out_edges(mat[i], 0) for i in range(vnum)]
        self._vnum = vnum  # 节点数目
        self._unconn = unconn
        self.DFS_seqs = []

    def get_edge(self, vi, vj):
        """获取两点之间边的权重"""
        if self.is_invalid(vi) or self.is_invalid(vi):
            raise GraphError('结点非法')
        for con_info in self._mat[vi]:
            if con_info[0] == vj:
                return con_info[1]
        return self._unconn

    def out_edges(self, vi):
        """返回能结点的所有关联边"""
        if self.is_invalid(vi):
            raise GraphError("结点非法")
        return self._mat[vi]

    def dfs_graph(self, vi):
        visited = [None] * self._vnum
        visited[0] = 1
        order = []
        length = 0
        stack = [(vi, v, w) for v, w in self.out_edges(vi)]  # 前节点、后节点、权重
        while stack and length < self._vnum:
            vi, vj, wj = stack.pop()
            if not visited[vj]:
                visited[vj] = 1
                order.append((vi, vj))
                length += 1
                stack.extend([(vj, vk, w) for vk, w in self.out_edges(vj)])
        return order

    def dfs_recur(self, v):
        visited = [0] * self._vnum
        visited[0] = 1
        order = []
        length = 0
        def dfs(v):
            nonlocal length
            if length == self._vnum:
                return
            for vj, w in self.out_edges(v):
                if not visited[vj]:
                    visited[vj] = 1
                    order.append((v, vj))
                    length += 1
                    dfs(vj)
        dfs(v)
        return order

    def kruskal(self):
        """边表统计，据权重排序---跨域判断---合并、刷新代表"""
        rep = list(range(self._vnum))  # 代表元初始化
        edges, mst = [], []
        for i in range(self._vnum):  # 边表统计
            edge = self.out_edges(i)  # i是源点，edge是目标点，权重的元组列表
            for e in edge:
                edges.append((e[1], i, e[0]))
        edges.sort(reverse=True)

        while edges:
            w, vi, vj = edges.pop()
            if rep[vi] != rep[vj]:  # 跨域判断
                rep[vj] = rep[vi]
                mst.append((vi, vj, w))
                if len(mst) == self._vnum-1:
                    break

                for j in range(len(rep)):  # 代表元刷新
                    if rep[j] == rep[vj]:
                        rep[j] = rep[vi]
        return mst

    def prim(self):
        """求已知和未知之间的最短路径"""

        count = 0
        cans = [(0,0,0)]
        mst = [0] * self._vnum

        while cans and count < self._vnum:
            w, vi, vj = cans.pop()
            if mst[vj]:
                continue
            mst[vj] = ((vi, vj), w)  # 扩展连通区
            count += 1

            for vk, w_ in self.out_edges(vj):
                if not mst[vk]:
                    # 扩展非联通区
                    cans.append((w_, vj, vk))
            cans.sort(reverse=True)

        return mst

    def dijkstra(self, v):
        """类似于prim算法，只是路径要累加"""
        cans = [(0,v,v)]
        mst = [0] * self._vnum
        count = 0

        while count < self._vnum and cans:
            length, vi, vj = cans.pop()
            if mst[vj]:
                continue
            mst[vj] = ((vi, vj), length)
            count += 1

            for vk, w_ in self.out_edges(vj):
                if not mst[vk]:
                    cans.append((length + w_, vj, vk))
            cans.sort(reverse=True)
        return mst


mat = [
    [0, 1, 4, 3],
    [1, 0, 0, 1],
    [4, 0, 0, 2],
    [3, 1, 2, 0]
]

g2 = GraphAL(mat=mat)

# print(g2)

# print(g2.dfs_graph(0))

# print(g2.dfs_recur(0))

# print(g2.kruskal())
#
# print(g2.prim())
#
# print(g2.dijkstra(0))  # 前一节点，最短路径元组
#
# print(g2.topo_sort())