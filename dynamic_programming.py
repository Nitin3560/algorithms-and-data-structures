from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list) 
        self.vertices = vertices 

    def add_edge(self, u, v):
        self.graph[u].append(v) 

    def topological_sort(self):
        visited = set()
        result = []

        def dfs(vertex):
            visited.add(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)
            result.append(vertex)

        for vertex in self.vertices:
            if vertex not in visited:
                dfs(vertex)
        return result[::-1]

vertices = ["s", "t", "x", "z", "y", "w", "v", "u"]
g = Graph(vertices)
edges = [
    ("s", "v"), ("s", "w"),
    ("t", "w"), ("t", "x"),
    ("v", "y"),
    ("w", "y"), ("w", "z"),
    ("x", "z"),
    ("y", "u"),
    ("z", "u")
]

for u, v in edges:
    g.add_edge(u, v)

def test_dfs():
    from collections import defaultdict

    class Graph:
        def __init__(self, vertices):
            self.graph = defaultdict(list)
            self.vertices = vertices

        def add_edge(self, u, v):
            self.graph[u].append(v)
            self.graph[v].append(u)

        def dfs_util(self, v, visited):
            visited[v] = True
            print(f"{v} ", end="")
            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    self.dfs_util(neighbor, visited)

        def dfs(self, start_vertex):
            visited = {v: False for v in self.graph}
            self.dfs_util(start_vertex, visited)

    g = Graph(6)
    g.add_edge("u", "v")
    g.add_edge("u", "x")
    g.add_edge("x", "v")
    g.add_edge("v", "y")
    g.add_edge("w", "y")
    g.add_edge("w", "z")
    g.add_edge("z", "y")

    print("DFS Traversal:")
    g.dfs("u")

def test_kruskal():
    class Graph:
        def __init__(self, vertices):
            self.vertices = vertices
            self.edges = []

        def add_edge(self, u, v, weight):
            self.edges.append((weight, u, v))

        def find_parent(self, parent, vertex):
            if parent[vertex] != vertex:
                parent[vertex] = self.find_parent(parent, parent[vertex])
            return parent[vertex]

        def union(self, parent, rank, x, y):
            root_x = self.find_parent(parent, x)
            root_y = self.find_parent(parent, y)
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

        def kruskal_mst(self):
            self.edges.sort()
            parent = {v: v for v in self.vertices}
            rank = {v: 0 for v in self.vertices}
            mst = []

            for weight, u, v in self.edges:
                root_u = self.find_parent(parent, u)
                root_v = self.find_parent(parent, v)
                if root_u != root_v:
                    mst.append((u, v, weight))
                    self.union(parent, rank, root_u, root_v)

            return mst

    vertices = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    g = Graph(vertices)
    g.add_edge("a", "b", 4)
    g.add_edge("a", "h", 8)
    g.add_edge("b", "h", 11)
    g.add_edge("b", "c", 8)
    g.add_edge("c", "d", 7)
    g.add_edge("c", "f", 4)
    g.add_edge("c", "i", 2)
    g.add_edge("d", "e", 9)
    g.add_edge("d", "f", 14)
    g.add_edge("e", "f", 10)
    g.add_edge("f", "g", 2)
    g.add_edge("g", "h", 1)
    g.add_edge("g", "i", 6)
    g.add_edge("h", "i", 7)

    print("Kruskal's MST :")
    mst = g.kruskal_mst()
    for u, v, weight in mst:
        print(f"{u} -- {v} == {weight}")

top_order = g.topological_sort()
print("Topological Sort Order:")
print(" ,".join(top_order))
test_dfs()
print()
test_kruskal()
