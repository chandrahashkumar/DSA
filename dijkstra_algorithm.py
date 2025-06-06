import heapq
def dijkstra(graph, start):
    # Create a dictionary to  store the  shortest distances from the start node
    shortest_distance = {node: float('infinity') for node in graph}
    shortest_distance[start] = 0
    # Create a priority queue to keep track of nodes to visit
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current distance is greater than the stored distance, skip it
        if current_distance > shortest_distance[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path is found, update the shortest distance
            if distance < shortest_distance[neighbor]:
                shortest_distance[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_distance

graph = {
    'A': {'B':1, 'C':4},
    'B': {'A':1, 'C':2, 'D':5},
    'C': {'A':4, 'B':2, 'D':1},
    'D': {'B':5, 'C':1}
}
start_node = 'A'
shortest_distance = dijkstra(graph, start_node)
print(f"Shortest distances from node {start_node}")
for node, distance in shortest_distance.items():
    print(f"To node {node}: {distance}")