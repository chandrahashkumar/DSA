from collections import deque

def is_bipartite(graph, V):
    color = [-1] * V  # -1 means uncolored

    for start in range(V):
        if color[start] == -1:
            queue = deque()
            queue.append(start)
            color[start] = 0  # Start coloring with 0

            while queue:
                u = queue.popleft()

                for v in graph[u]:
                    if color[v] == -1:
                        # Assign alternate color to this adjacent vertex
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        # Adjacent vertex has same color → Not Bipartite
                        print("Graph is NOT Bipartite")
                        return False

    print("Graph is Bipartite")
    return True

# Example Usage:
if __name__ == "__main__":
    # Number of vertices
    V = 6

    # Adjacency list representation of graph
    graph = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2, 4],
        4: [3, 5],
        5: [4]
    }

    is_bipartite(graph, V)
