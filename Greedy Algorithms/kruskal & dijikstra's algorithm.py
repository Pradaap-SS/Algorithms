'''Kruskal's Algorithm:
Kruskal's Algorithm is a greedy algorithm for finding the minimum spanning tree of a weighted undirected graph. 
It starts with an empty set of edges and adds the next cheapest edge that does not form a cycle.
'''

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        
        if x_root == y_root:
            return
        
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

def kruskal(graph):
    n = len(graph)
    edges = []
    for u in range(n):
        for v, weight in graph[u]:
            edges.append((u, v, weight))
    
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    minimum_spanning_tree = []
    disjoint_set = DisjointSet(n)
    
    for u, v, weight in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            minimum_spanning_tree.append((u, v, weight))
            disjoint_set.union(u, v)
    
    return minimum_spanning_tree

# Example usage:
graph = [
    [(0, 1), (0, 2), (1, 2)],  # Edges and weights for vertex 0
    [(0, 1)],                 # Edges and weights for vertex 1
    [(0, 2), (1, 2)]          # Edges and weights for vertex 2
]
minimum_spanning_tree = kruskal(graph)
print(minimum_spanning_tree)

'''
Time Complexity: The time complexity of this algorithm is O(E log V), where E is the number of edges and V is the number of vertices. 
Sorting the edges takes O(E log E) time, and each find and union operation takes nearly constant time.

Space Complexity: The space complexity is O(V), where V is the number of vertices. 
This is because the algorithm uses additional space to store the parent and rank arrays for the disjoint set.
'''


'''
Dijkstra's Algorithm:
Dijkstra's Algorithm is a greedy algorithm for finding the shortest path between two vertices in a weighted graph. 
It starts from a source vertex and iteratively selects the vertex with the smallest distance.
'''


import heapq

def dijkstra(graph, source):
    n = len(graph)
    distances = [float('inf')] * n
    distances[source] = 0
    pq = [(0, source)]  # Priority queue of (distance, vertex)
    
    while pq:
        distance, u = heapq.heappop(pq)
        
        if distance > distances[u]:
            continue
        
        for v, weight in graph[u]:
            new_distance = distance + weight
            if new_distance < distances[v]:
                distances[v] = new_distance
                heapq.heappush(pq, (new_distance, v))
    
    return distances

# Example usage:
graph = [
    [(1, 4), (2, 1)],           # Edges and weights for vertex 0
    [(0, 4), (2, 2), (3, 5)],   # Edges and weights for vertex 1
    [(0, 1), (1, 2), (3, 8)],   # Edges and weights for vertex 2
    [(1, 5), (2, 8)]            # Edges and weights for vertex 3
]
source = 0
distances = dijkstra(graph, source)
print(distances)


'''
Time Complexity: The time complexity of this algorithm is O((V + E) log V), 
where V is the number of vertices and E is the number of edges. 
Each vertex can be inserted and extracted from the priority queue at most once, which takes O(log V) time.

Space Complexity: The space complexity is O
'''


