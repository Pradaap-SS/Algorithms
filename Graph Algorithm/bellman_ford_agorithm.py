'''
Bellman-Ford Algorithm (Shortest Path with Negative Weights):
The Bellman-Ford Algorithm is used to find the shortest path from a single source vertex to 
all other vertices in a graph that may contain negative-weight edges. It iteratively relaxes 
the edges to find the shortest paths.
'''
def bellman_ford(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight
    
    # Check for negative-weight cycles
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if distances[vertex] + weight < distances[neighbor]:
                raise ValueError("Graph contains negative-weight cycles")
    
    return distances

# Example graph represented as an adjacency list with weights
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': -5},
    'C': {'A': 2, 'D': 1},
    'D': {'B': -5, 'C': 1}
}

start_vertex = 'A'
distances = bellman_ford(graph, start_vertex)

print("Shortest distances from vertex", start_vertex + ":")
for vertex, distance in distances.items():
    print(vertex + ":", distance)


'''
Time Complexity: The time complexity of the Bellman-Ford Algorithm is O(V * E), 
where V is the number of vertices and E is the number of edges in the graph.

Space Complexity: The space complexity is O(V), where V is the number of vertices, 
as it uses a distances dictionary to store the shortest distances.
'''