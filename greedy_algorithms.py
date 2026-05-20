import heapq

def dijkstra(graph, source):
    priority_queue = [(0, source)]
    shortest_distances = {source: 0}
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph.get(current_node, []):
            distance = current_distance + weight
            if neighbor not in shortest_distances or distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_distances


def bellman_ford(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                return "Negative weight cycle"

    return distances

def floyd_warshall(graph, vertices):
    distances = {u: {v: float('inf') for v in vertices} for u in vertices}
    for u in graph:
        for v in graph[u]:
            distances[u][v] = graph[u][v]
    for v in vertices:
        distances[v][v] = 0

    for k in vertices:
        for i in vertices:
            for j in vertices:
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    return distances

# Example for Dijkstra's Algorithm
graph_example = {
    's': [('t', 10), ('y', 5)],
    't': [('x', 1), ('y', 2)],
    'x': [('z', 4)],
    'y': [('t', 3), ('x', 9), ('z', 2)],
    'z': [('s', 7), ('x', 6)],
}

source_node = 's'
shortest_paths = dijkstra(graph_example, source_node)
print(shortest_paths)


# Example for Bellman-ford'S Algorithm
graph_example_bf = {
    's': [('t', 10), ('y', 5)],
    't': [('x', 1), ('y', 2)],
    'x': [('z', 4)],
    'y': [('t', 3), ('x', 9), ('z', 2)],
    'z': [('s', 7), ('x', 6)],
}

source_node_bf = 's'
shortest_paths_bf = bellman_ford(graph_example_bf, source_node_bf)
print(shortest_paths_bf)

# Example for Floyd Warshall's Algorithm
graph_example_fw = {
    's': {'t': 10, 'y': 5},
    't': {'x': 1, 'y': 2},
    'x': {'z': 4},
    'y': {'t': 3, 'x': 9, 'z': 2},
    'z': {'s': 7, 'x': 6},
}
vertices_example = ['s', 't', 'x', 'y', 'z']
shortest_paths_fw = floyd_warshall(graph_example_fw, vertices_example)
print(shortest_paths_fw)
