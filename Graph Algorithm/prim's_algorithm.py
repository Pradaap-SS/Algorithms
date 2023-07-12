'''
Prim's Algorithm (Minimum Spanning Tree):
Prim's Algorithm is used to find the minimum spanning tree of a connected, 
undirected graph. It starts with a single vertex and iteratively adds the 
edges with the smallest weights that connect to the existing tree.
'''

import heapq

def prim(graph):
    minimum_spanning_tree = []
    visited = set()
    start_vertex = list(graph.keys())[0]
    visited.add(start_vertex)
    edges = [
        (weight, start_vertex, neighbor)
        for neighbor, weight in graph[start_vertex].items()
    ]
    heapq.heapify(edges)
    
    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            minimum_spanning_tree.append((u, v, weight))
            
            for neighbor, weight in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (weight, v, neighbor))
    
    return minimum_spanning_tree

# Example graph represented as an adjacency list with weights
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8},
    'D': {'B': 5, 'C': 8}
}

minimum_spanning_tree = prim(graph)

print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)


'''
Time Complexity: The time complexity of Prim's Algorithm is O((V + E) * log V), 
where V is the number of vertices and E is the number of edges in the graph.

Space Complexity: The space complexity is O(V), where V is the number of vertices, 
as it uses a visited set and a heap to store the edges.
'''