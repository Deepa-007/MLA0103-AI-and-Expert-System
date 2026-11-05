
from lab_utils import start, ask, finish
import heapq

start("program3_output.txt")
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('F', 3)],
    'E': [('F', 1)],
    'F': []
}

pq = [(0, 'A', ['A'])]
best = {}
found = False

while pq:
    cost, node, path = heapq.heappop(pq)

    if cost >= best.get(node, float('inf')):
        continue
    best[node] = cost

    if node == 'F':
        print("Least-cost path:", path)
        print("Total cost:", cost)
        found = True
        break

    for neighbor, weight in graph[node]:
        heapq.heappush(
            pq, (cost + weight, neighbor, path + [neighbor])
        )

if not found:
    print("Path not found")

finish()
