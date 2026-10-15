
from lab_utils import start, ask, finish

start("program18_output.txt")

color = ask("Enter fruit color: ").lower()

if color == "yellow":
    print("Possible fruit: Banana")
elif color == "orange":
    print("Possible fruit: Orange")
elif color == "red":
    print("Possible fruit: Apple or Strawberry")
elif color == "green":
    print("Possible fruit: Green apple")
else:
    print("Fruit not identified")

finish()
