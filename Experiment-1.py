
from lab_utils import start, ask, finish
from collections import deque

start("program1_output.txt")
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': ['F'], 'F': []
}

goal = ask("Enter goal node (F): ") or "F"
queue = deque([['A']])
visited = set()
found = False

while queue:
    path = queue.popleft()
    node = path[-1]

    if node == goal:
        print("Shortest path:", path)
        found = True
        break

    if node not in visited:
        visited.add(node)
        for neighbor in graph.get(node, []):
            queue.append(path + [neighbor])

if not found:
    print("Path not found")

finish()
