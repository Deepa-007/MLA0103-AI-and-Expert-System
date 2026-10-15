
from lab_utils import start, ask, finish

start("program20_output.txt")

people = {
    "dharshini": "2007-06-13",
    "deepa": "2007-06-27",
    "divya": "2008-01-31"
}

name = ask("Enter person name: ").lower()

if name in people:
    print("Date of birth:", people[name])
else:
    print("Person not found")

finish()
