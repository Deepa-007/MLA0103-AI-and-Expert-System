
from lab_utils import start, ask, finish

start("program21_output.txt")

numbers = list(map(
    int, ask("Enter numbers separated by spaces: ").split()
))

if len(numbers) < 2:
    print("Enter at least two numbers")
elif all(x == numbers[0] for x in numbers):
    print("Repeated pattern")
elif all(numbers[i] < numbers[i+1]
         for i in range(len(numbers)-1)):
    print("Increasing pattern")
elif all(numbers[i] > numbers[i+1]
         for i in range(len(numbers)-1)):
    print("Decreasing pattern")
else:
    print("Irregular pattern")

finish()
