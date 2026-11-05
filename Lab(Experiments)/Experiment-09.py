
from lab_utils import start, finish
from collections import deque

start("program9_output.txt")

queue = deque([((0, 0), [])])
visited = set()
solution = None

while queue:
    (a, b), path = queue.popleft()

    if (a, b) in visited:
        continue
    visited.add((a, b))

    path = path + [(a, b)]

    if a == 2:
        solution = path
        break

    pour_ab = min(a, 3 - b)
    pour_ba = min(b, 4 - a)

    states = [
        (4, b), (a, 3), (0, b), (a, 0),
        (a - pour_ab, b + pour_ab),
        (a + pour_ba, b - pour_ba)
    ]

    for state in states:
        if state not in visited:
            queue.append((state, path))

if solution:
    print("Jug states (4L jug, 3L jug):")
    for state in solution:
        print(state)
else:
    print("Solution not found")

finish()
