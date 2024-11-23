from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set()
    traversal = []
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        traversal.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return traversal
graph = {
    'A': ['B', 'C'],
    
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
result = bfs(graph, 'A')
print("BFS Traversal:", result)
