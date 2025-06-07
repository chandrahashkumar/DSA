'''
def dfs_recursive(graph,vertex, visited):
    if vertex not in visited:
        print(vertex,end=' ')
        visited.add(vertex)
        for neighbor in graph[vertex]:
            dfs_recursive(graph,neighbor,visited)



graph ={
    'A':['B','C'],
    'B':['A','D','E'],
    'D':['B'],
    'C':['A','F'],
    'E':['B','F'],
    'F':['C','E']
}

start_vertex = 'A'
visited = set()
print(f"DFS (Recursive) starting from: {start_vertex}")
dfs_recursive(graph,start_vertex,visited)

'''


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            stack.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)


graph ={
    'A':['B','C'],
    'B':['A','D','E'],
    'D':['B'],
    'C':['A','F'],
    'E':['B','F'],
    'F':['C','E']
}

start_vertex = 'A'
print(f"DFS (Recursive) starting from: {start_vertex}")
dfs_iterative(graph,start_vertex)