
from lab_utils import start, ask, finish

start("program2_output.txt")
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}
visited = set()

def dfs(node):
    if node not in visited:
        visited.add(node)
        print(node, end=" ")
        for neighbor in graph[node]:
            dfs(neighbor)

print("DFS traversal:")
dfs('A')
print()
finish()
