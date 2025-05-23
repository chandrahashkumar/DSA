class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph =[]
    def add_edge(self,u,v,w):
         self.graph.append([u,v,w])
    def bellman_ford(self,src):
        # Initialize distances to all vertices as infinity and the source as 0
        distances = [float("Inf")] * self.V
        distances[src] = 0
        # Relax all edges |V| -1 times
        for _ in range(self.V -1):
            for u,v,w in self.graph:
                if distances[u] != float("Inf") and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

        # Check for negative weight cycles
        for u,v,w in self.graph:
            if distances[u] != float("Inf") and distances[u] + w < distances[v]:
                print("Graph contains negative weight cycle")
                return

        # Print the shortest distances
        for i in range(self.V):
            print(f"Distance from {src} to {i} is {distances[i]}")

# Example usage

if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(0,1,-1)
    graph.add_edge(0,2,4)
    graph.add_edge(1,2,3)
    graph.add_edge(1,3,2)
    graph.add_edge(1,4,2)
    graph.add_edge(3,2,5)
    graph.add_edge(3,1,10)
    graph.add_edge(4,3,-3)

    graph.bellman_ford(0)


