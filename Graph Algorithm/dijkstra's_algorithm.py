'''
Dijkstra's Algorithm (Shortest Path):
Dijkstra's Algorithm is used to find the shortest path from a single source vertex to 
all other vertices in a weighted graph. It maintains a priority queue (min-heap) to select
the vertex with the minimum distance from the source.
'''

import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    heap = [(0, start)]
    
    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    
    return distances

# Example graph represented as an adjacency list with weights
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5},
    'C': {'A': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)

print("Shortest distances from vertex", start_vertex + ":")
for vertex, distance in distances.items():
    print(vertex + ":", distance)


'''
Time Complexity: The time complexity of Dijkstra's Algorithm is O((V + E) log V), 
where V is the number of vertices and E is the number of edges in the graph.

Space Complexity: The space complexity is O(V), where V is the number of vertices, 
as it uses a distances dictionary to store the shortest distances.
'''