'''
Kruskal's Algorithm (Minimum Spanning Tree):
Kruskal's Algorithm is used to find the minimum spanning tree of a connected, 
undirected graph. It starts with an empty spanning tree and iteratively adds 
the edges with the smallest weights that do not create a cycle.
'''

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1

def kruskal(graph):
    mst = []
    disjoint_set = DisjointSet(graph.keys())
    edges = []
    
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            edges.append((weight, vertex, neighbor))
    
    edges.sort()  # Sort edges in ascending order of weight
    
    for weight, v1, v2 in edges:
        if disjoint_set.find(v1) != disjoint_set.find(v2):
            mst.append((v1, v2, weight))
            disjoint_set.union(v1, v2)
    
    return mst

# Example graph represented as an adjacency list with weights
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8},
    'D': {'B': 5, 'C': 8}
}

minimum_spanning_tree = kruskal(graph)

print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)


'''
Time Complexity: The time complexity of Kruskal's Algorithm is O(E * log E), 
where E is the number of edges in the graph.

Space Complexity: The space complexity is O(V), where V is the number of vertices, 
as it uses a disjoint set data structure to track the connected components.
'''