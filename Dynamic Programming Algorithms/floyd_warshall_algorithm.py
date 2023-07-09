'''
Floyd-Warshall Algorithm (Shortest Path):
The Floyd-Warshall algorithm is used to find the shortest path between all pairs of vertices in a weighted directed graph. 
It handles both positive and negative edge weights but assumes no negative cycles. The algorithm uses a dynamic programming 
approach to compute the shortest path distances by considering all possible intermediate vertices.
'''

INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    dist = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j] if graph[i][j] != 0 else INF
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

shortest_paths = floyd_warshall(graph)
print("Shortest paths:")
for row in shortest_paths:
    print(row)

'''
Shortest paths:
[0, 5, 8, 9]
[INF, 0, 3, 4]
[INF, INF, 0, 1]
[INF, INF, INF, 0]
'''

'''
Time Complexity: The time complexity of the Floyd-Warshall algorithm is O(n^3), where n is the number of vertices 
in the graph. It involves three nested loops to iterate over all vertices and compute the shortest distances.

Space Complexity: The space complexity is O(n^2) since it requires a 2D array of size n * n to store the distances
between all pairs of vertices.
'''