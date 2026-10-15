
from lab_utils import start, finish

start("program7_output.txt")

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': 3, 'E': 5, 'F': 2, 'G': 9
}

def minimax(node, maximizing):
    if isinstance(tree[node], int):
        return tree[node]

    values = [minimax(child, not maximizing)
              for child in tree[node]]

    return max(values) if maximizing else min(values)

print("Best value:", minimax('A', True))
finish()
