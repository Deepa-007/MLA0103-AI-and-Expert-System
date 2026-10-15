
from lab_utils import start, finish

start("program15_output.txt")

parent = [
    ("Ravi", "Arun"),
    ("Ravi", "Meena"),
    ("Arun", "Kiran"),
    ("Arun", "Priya")
]

def is_parent(x, y):
    return (x, y) in parent

def is_grandparent(x, z):
    for a, b in parent:
        if a == x and is_parent(b, z):
            return True
    return False

def is_sibling(x, y):
    if x == y:
        return False
    for p, child in parent:
        if child == x and is_parent(p, y):
            return True
    return False

print("Ravi is grandparent of Kiran:",
      is_grandparent("Ravi", "Kiran"))
print("Kiran and Priya are siblings:",
      is_sibling("Kiran", "Priya"))

finish()
