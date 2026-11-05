
from lab_utils import start, ask, finish
import heapq

start("program6_output.txt")
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('F', 3)],
    'E': [('F', 1)], 'F': []
}
h = {'A': 4, 'B': 4, 'C': 2, 'D': 3, 'E': 1, 'F': 0}

pq = [(h['A'], 0, 'A', ['A'])]
best = {'A': 0}
found = False

while pq:
    _, cost, node, path = heapq.heappop(pq)

    if cost != best.get(node):
        continue

    if node == 'F':
        print("Optimal path:", path)
        print("Total cost:", cost)
        found = True
        break

    for neighbor, weight in graph[node]:
        new_cost = cost + weight

        if new_cost < best.get(neighbor, float('inf')):
            best[neighbor] = new_cost
            heapq.heappush(
                pq, (new_cost + h[neighbor], new_cost,
                     neighbor, path + [neighbor])
            )

if not found:
    print("Path not found")

finish()
