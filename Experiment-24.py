
from lab_utils import start, finish

start("program24_output.txt")

facts = {"power_connected", "computer_not_starting"}

rules = {
    "possible_hardware_fault": [
        "computer_not_starting", "power_connected"
    ],
    "check_hardware": ["possible_hardware_fault"]
}

def backward_chaining(goal):
    if goal in facts:
        return True

    if goal not in rules:
        return False

    return all(backward_chaining(item) for item in rules[goal])

goal = "check_hardware"

if backward_chaining(goal):
    print("Goal proved:", goal)
else:
    print("Goal cannot be proved")

finish()
