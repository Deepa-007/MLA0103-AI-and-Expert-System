
from lab_utils import start, finish

start("program8_output.txt")

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': 3, 'E': 5, 'F': 2, 'G': 9
}

def alphabeta(node, alpha, beta, maximizing):
    if isinstance(tree[node], int):
        return tree[node]

    if maximizing:
        value = float('-inf')
        for child in tree[node]:
            value = max(value, alphabeta(
                child, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    value = float('inf')
    for child in tree[node]:
        value = min(value, alphabeta(
            child, alpha, beta, True))
        beta = min(beta, value)
        if alpha >= beta:
            break
    return value

result = alphabeta('A', float('-inf'), float('inf'), True)
print("Best value:", result)
finish()
