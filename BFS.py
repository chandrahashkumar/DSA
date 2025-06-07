from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

graph ={
    'A':['B','C'],
    'B':['A','D','E'],
    'D':['B'],
    'C':['A','F'],
    'E':['B','F'],
    'F':['C','E']
}

start_vertex = 'A'
print(f"BFS starting from : {start_vertex}" )
bfs(graph,start_vertex)
