
from lab_utils import start, finish

start("program23_output.txt")

facts = {"computer_not_starting", "power_connected"}

rules = [
    ({"computer_not_starting", "power_connected"},
     "possible_hardware_fault"),
    ({"possible_hardware_fault"}, "check_hardware")
]

changed = True

while changed:
    changed = False

    for conditions, result in rules:
        if conditions.issubset(facts) and result not in facts:
            facts.add(result)
            print("Derived:", result)
            changed = True

print("Final facts:", facts)
finish()
