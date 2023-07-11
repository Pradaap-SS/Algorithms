'''
DFS is an algorithm for traversing or searching a graph in a depthward motion. It explores as far as possible along each branch before backtracking. 
DFS uses a stack or recursion to keep track of the vertices to visit next.
'''

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    
    for neighbor in graph[start] - visited:
        dfs(graph, neighbor, visited)

# Example graph represented as an adjacency list
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

print("DFS traversal:")
dfs(graph, 'A')


'''
Time Complexity: The time complexity of DFS is O(V + E), where V is the number of vertices and E 
is the number of edges in the graph.

Space Complexity: The space complexity is O(V), where V is the number of vertices, due to the recursion 
stack and the visited set.
'''