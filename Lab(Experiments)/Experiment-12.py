
from lab_utils import start, ask, finish

start("program12_output.txt")

income = ask("Income (low/high): ").lower()
credit = ask("Credit history (good/bad): ").lower()

if income == "high" and credit == "good":
    print("Loan approved")
elif credit == "bad":
    print("Loan rejected")
elif income == "low":
    print("Loan rejected")
else:
    print("Invalid input")

finish()
