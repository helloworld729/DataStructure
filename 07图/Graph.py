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
        return "[\n" + ",\n".join(map(str, self._mat)) + "\n]" +  "\nunconn: " + str(self._unconn)
              
    
    def   out_edges(self, vi):
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
    
    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1 # 返回新增结点编号（从0开始）
    
    def add_edge(self, vi, vj, val=1):
        """更新/增加边"""
        if not self.is_invalid(vi) and not self.is_invalid(vj):            
            row = self._mat[vi]
            i = 0
            while i < len(row):
                if vj == row[i][0]:  # 结点已经存在，更新
                    self._mat[vi][i] = (vj, val)
                    return
                if vj < i:  # 没有该结点
                    break
                i += 1
            self._mat[vi].insert(i, (vj, val))  # 创建新结点
        else:
            raise GraphError("结点非法")
    
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
    
    def DFS_graph(self, v0):
        """非递归深度优先"""
        visited = [0] * self._vnum  # 访问过的结点记录
        visited[v0] = 1
        DFS_seq = [v0]  # v0作为第一个访问过的节点
        st = []  # 此处当做堆栈使用
        st.append((0, self.out_edges(v0)))  # 接下来要从边表访问的点在边表中的索引，边表
        count = 0
        while st:
            count += 1
            i, edges = st.pop()  # 访问序号、边表信息
            if i < len(edges):
                v, e = edges[i]  # 邻接点和边信息
                st.append((i+1, edges)) # 同一边表中下一次要访问的点
                
                if not visited[v]:
                    visited[v] = 1
                    DFS_seq.append(v)
                    st.append((0, self.out_edges(v)))  # 深度推进
        print(count)
        return DFS_seq
    
    def DFS_recur(self, v, visited = {}):
        """基于递归的深度优先"""
        if v not in visited:  # 处理办法
            self.DFS_seqs.append(v)
            visited[v] = 1
            
        edges = self.out_edges(v)  # 边表
        vertexs = [e[0] for e in edges]   # 具体的邻接点
        diff = [v for v in vertexs if v not in visited]  # 还没有访问过的邻接点列表
        if not diff:  # 边界条件
            return
            
        for v in diff:  # 递归推进
            self.DFS_recur(v, visited)
            
        return self.DFS_seqs
    
    def DFS_span_forest(self):
        """深度遍历生成树"""
        span_forest = [None] * self._vnum
        
        def dfs(self, v):  # 递归遍历函数，在递归中记录经由边
            nonlocal span_forest
            for u, w in self.out_edges(v):  # (目标点， 权重)
                if span_forest[u] is None:
                    span_forest[u] = (v, w)
                    dfs(self, u)
                    
        for v in range(self._vnum):  # 考虑非联通???
            if span_forest[v] is None:
                span_forest[v] = (v, 0)  # 边信息为0，树根结点
                dfs(self, v)
        return span_forest
    
    def Kruskal(self):
        """最小生成树算法"""
        vnum = self._vnum
        reps = [i for i in range(vnum)]  # 各个元素的代表元初始化为自己
        mst, edges = [], []  # 最小生成树， 边集合
        
        for vi in range(vnum):               # 边表统计
            for v, w in self.out_edges(vi):  # 目标点、权重
                edges.append((w, vi, v))     # 权重、源点、终点
        edges.sort()  # 最小-->权重最小
        
        for w, vi, vj in edges:
            if reps[vi] != reps[vj]:  # 在不同的连通区
                mst.append(((vi, vj), w))
                if len(mst) == vnum - 1:  # 边界条件
                    break
                rep, orep = reps[vi], reps[vj]
                for i in range(vnum):  # 刷新代表元
                    if reps[i] == orep:
                        reps[i] = rep
        return mst
    
    def Prim(self):
        vnum = self._vnum
        mst = [None] * vnum  # 当前连通区
        cans = [(0,0,0)]  # 记录候选边（w, vi, vj）
        count = 0  # 当前连通区节点数量
        
        while count < vnum and cans:
            w, vi, vj = cans.pop()  # 取当时最小边
            if mst[vj]:
                continue
            mst[vj]=((vi, vj),w)  # u是当前连通区、v是目标连通区
            count += 1
            
            for vk, w_ in self.out_edges(vj):
                if not mst[vk]:
                    cans.append((w_, vj, vk))
            cans.sort(reverse=True)  # 不要用内嵌函数sorted，易出错
        return mst
    
    def dijkstra(self, v0):  # 最短路径
        vnum = self._vnum
        paths = [None] * vnum # （前一节点， 最短路径长度）元组列表
        cans = [(0,v0,v0)]  # 记录候选边（路径长度，候选节点前一节点， 当前候选节点）
        count = 0  # 当前连通区节点数量
        
        while count < vnum and cans:
            plen, u, v_current = cans.pop()  # 最短路径长度， 前一顶点， 候选顶点
            if paths[v_current]:  # 路径长度已经确定
                continue
            paths[v_current]=(u, plen)  # 将前一顶点和最短路径保存，意思是候选节点加入到连通区
            count += 1
            
            for v, w in self.out_edges(v_current):  # 生成候选集，v是目标点 w是两点间边的权值
                if not paths[v]:
                    cans.append((plen + w, v_current, v))
            cans.sort(reverse=True)

        return paths  
    
    def topo_sort(self):
        """拓扑排序"""
        vnum = self._vnum
        indegree, toposeq = [0] * vnum, []  # 入度表 和 拓扑序列
        zerov = -1  # 零度点索引初始化
        
        for vi in range(vnum):  # 建立初始的入度表
            for v, w in self.out_edges(vi):
                indegree[v] += 1
        print('入度表',indegree)
                
        for vi in range(vnum):  # 建立初始的零度表
            if indegree[vi] == 0:
                indegree[vi] = zerov  # 上一零度点索引（由于边表索引隐含为结点，所以也可以理解为结点）
                zerov = vi  # 零度索引绑定到自己
        print('当前零度点位置', zerov)                
                
        for n in range(vnum+1):
            if zerov == -1:
                return toposeq   # 没有入度为0的点，返回False
            vi = zerov  # 当前访问的0度点
            zerov = indegree[zerov] # 下一待访问0度点
            toposeq.append(vi)

            for v, w in self.out_edges(vi):
                indegree[v] -= 1  # 关联节点入度减1
                if  indegree[v] == 0:
                    indegree[v] = zerov  # 指向前面的待访问零度点
                    zerov = v

mat = [
[0, 1, 4, 3],
[1, 0, 0, 1],
[4, 0, 0, 2],
[3, 1, 2, 0]
]
g2 = GraphAL(mat=mat)
# print(g2)

# for i in range(3):  # 非递归深度优先遍历
#     print(g2.DFS_graph(i))


# g2.DFS_seqs=[]
# print(g2.DFS_recur(0))  # 如果不清空的话，jupyter 保存了visited变量

# print(g2.DFS_span_forest())
#
# print(g2.Kruskal())

# print(g2.Prim())
#
print(g2.dijkstra(0))  # 前一节点，最短路径元组
#
# print(g2.topo_sort())