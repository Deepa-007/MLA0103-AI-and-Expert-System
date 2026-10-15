
from lab_utils import start, ask, finish

start("program19_output.txt")

planets = {
    "mercury": (1, "Terrestrial"),
    "venus": (2, "Terrestrial"),
    "earth": (3, "Terrestrial"),
    "mars": (4, "Terrestrial"),
    "jupiter": (5, "Gas giant"),
    "saturn": (6, "Gas giant"),
    "uranus": (7, "Ice giant"),
    "neptune": (8, "Ice giant")
}

name = ask("Enter planet name: ").lower()

if name in planets:
    print("Position:", planets[name][0])
    print("Type:", planets[name][1])
else:
    print("Planet not found")

finish()
