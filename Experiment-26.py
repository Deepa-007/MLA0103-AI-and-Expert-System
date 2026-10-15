
from lab_utils import start, ask, finish

start("program26_output.txt")

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

n = int(ask("Enter N: "))

if n < 0:
    print("Enter a non-negative number")
else:
    print("Sum =", sum_n(n))

finish()
