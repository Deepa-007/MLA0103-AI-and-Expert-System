
from lab_utils import start, ask, finish
import heapq

start("program4_output.txt")
graph = {
    'A': ['B', 'C'],
    'B': ['D'], 'C': ['E'],
    'D': ['F'], 'E': ['F'], 'F': []
}
h = {'A': 5, 'B': 4, 'C': 2, 'D': 3, 'E': 1, 'F': 0}

pq = [(h['A'], 'A', ['A'])]
visited = set()
found = False

while pq:
    _, node, path = heapq.heappop(pq)

    if node in visited:
        continue
    visited.add(node)

    if node == 'F':
        print("Path:", path)
        found = True
        break

    for neighbor in graph[node]:
        if neighbor not in visited:
            heapq.heappush(
                pq, (h[neighbor], neighbor, path + [neighbor])
            )

if not found:
    print("Path not found")

finish()
