
from lab_utils import start, ask, finish

start("program10_output.txt")

def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(source, "->", destination)
        return

    hanoi(n-1, source, destination, auxiliary)
    print(source, "->", destination)
    hanoi(n-1, auxiliary, source, destination)

n = int(ask("Enter number of disks: "))

if n <= 0:
    print("Enter a positive number")
else:
    print("Moves:")
    hanoi(n, 'A', 'B', 'C')
    print("Minimum moves:", 2**n - 1)

finish()
