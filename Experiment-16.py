
from lab_utils import start, ask, finish

start("program16_output.txt")

birds = ["parrot", "sparrow", "penguin", "ostrich"]
cannot_fly = ["penguin", "ostrich"]

bird = ask("Enter bird name: ").lower()

if bird not in birds:
    print("Bird not found")
elif bird in cannot_fly:
    print(bird, "cannot fly")
else:
    print(bird, "can fly")

finish()
