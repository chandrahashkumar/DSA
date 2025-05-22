class Graph:
    def __init__(self, vertics):
        self.V = vertics
        self.graph = []
        
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
        
    def kruskal_mst(self):
        # Sort by weight (third element) instead of first element
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = [i for i in range(self.V)]
        result = []
        e = 0
        i = 0
        
        while e < self.V-1 and i < len(self.graph):
            # Correct order of unpacking: u, v, w instead of w, u, v
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, x, y)
        return result

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
        
    def union(self, parent, x, y):
        x_set = self.find(parent, x)
        y_set = self.find(parent, y)
        parent[x_set] = y_set

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)
    mst = g.kruskal_mst()
    print("Minimum Spanning Tree(Edge, Weight)")
    for u, v, w in mst:
        print(f"Edge: ({u}, {v}), Weight: {w}")