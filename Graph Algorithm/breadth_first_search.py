'''
Breadth-First Search (BFS):
BFS is an algorithm for traversing or searching a graph in a breadthward motion. 
It explores all the vertices of a graph at the same level before moving to the next level. 
BFS uses a queue to keep track of the vertices to visit next.'''

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            queue.extend(graph[vertex] - visited)

# Example graph represented as an adjacency list
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

print("BFS traversal:")
bfs(graph, 'A')


'''
Time Complexity: The time complexity of BFS is O(V + E), 
where V is the number of vertices and E is the number of edges in the graph.

Space Complexity: The space complexity is O(V), where V is the number of vertices, 
as the visited set and the queue can store at most V vertices.
'''