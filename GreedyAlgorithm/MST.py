import sys
import heapq
from functools import total_ordering
import copy


@total_ordering
class Edge(object):
    st, ed, value = 0, 0, 0

    def __init__(self, st, ed, value):
        self.st = st
        self.ed = ed
        self.value = value

    def __le__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return '(' + str(self.st) + ',' + str(self.ed) + ')'


class Graph:
    edge = None
    vertex = None

    def __init__(self, v, e):
        self.vertex = copy.copy(v)
        self.edge = copy.copy(e)
        for i in range(0, len(v)):
            e[i][i] = sys.maxsize

    def valid(self, i, j):
        return 0 <= i < len(self.vertex) and 0 <= j < len(self.vertex) and self.edge[i][j] is not sys.maxsize

    def get_edge(self, i, j):
        return Edge(i, j, self.edge[i][j])

    def set_edge(self, i, j, v):
        self.edge[i][j] = v

    def insert_vertex(self, vertex):
        for e in self.edge:
            e.append(None)
        self.edge.append([None] * len(self.vertex) + 1)
        return self.vertex.append(vertex)

    def next_nbr(self, i, j):

        while True:
            j = j - 1
            if -1 < j and not self.valid(i, j):
                continue
            break
        return j

    def first_nbr(self, i):
        return self.next_nbr(i, len(self.vertex))

    def prime(self):
        min_edge = Edge(0, 0, sys.maxsize)
        i = 0
        while i < len(self.vertex):
            j = self.first_nbr(i)
            while j > -1:
                if self.get_edge(i, j) < min_edge:
                    min_edge = self.get_edge(i, j)
                j = self.next_nbr(i, j)
            i = i + 1
        heap = []
        path = [min_edge.st]
        path_edge = []
        self.fin_all_vtx(min_edge.st, heap, path)
        while len(path) < len(self.vertex):
            current_edge = heapq.heappop(heap)
            path.append(current_edge.ed)
            path_edge.append(current_edge)
            self.fin_all_vtx(path[-1], heap, path)
        return path_edge

    def fin_all_vtx(self, vtx, heap, PATH):
        j = self.first_nbr(vtx)
        while j > -1:
            e = self.get_edge(vtx, j)
            heap.append(e)
            j = self.next_nbr(vtx, j)
        for i in heap:
            if i.ed in PATH:
                i.value = sys.maxsize
        heapq.heapify(heap)

    def kruskal(self):
        heap = []
        for i in range(0, len(self.vertex)):
            for j in range(0, i):
                heapq.heappush(heap, self.get_edge(i, j))
        union_branch = []
        edge_path = []
        for i in self.vertex:
            union_branch.append([i])
        while len(union_branch) > 1:
            current_edge = heapq.heappop(heap)
            ub1, ub2 = 0, 0
            for iub, ub in enumerate(union_branch):
                if current_edge.st in ub:
                    ub1 = iub
                if current_edge.ed in ub:
                    ub2 = iub
            if ub1 == ub2:
                continue
            union_branch[ub1] = union_branch[ub1] + union_branch[ub2]
            del union_branch[ub2]
            edge_path.append(current_edge)
        return edge_path


v = [0, 1, 2, 3, 4, 5]
nul = sys.maxsize
e = [
    [nul, 6, 1, 5, nul, nul],
    [6, nul, 5, nul, 3, nul],
    [1, 5, nul, 5, 6, 4],
    [5, nul, 5, nul, nul, nul, 2],
    [nul, 3, 6, nul, nul, 6],
    [nul, nul, 4, 2, 6, nul]
]

graph = Graph(v, e)
tree = graph.prime()
print('Prime:')
for t in tree:
    print(t, end=' ')
tree = graph.kruskal()
print('\nKruskal:')
for t in tree:
    print(t, end=' ')
