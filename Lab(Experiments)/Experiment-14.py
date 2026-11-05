
from lab_utils import start, ask, finish

start("program14_output.txt")

age = int(ask("Enter age: "))
bmi = float(ask("Enter BMI: "))
condition = ask("Condition (none/diabetes): ").lower()

if age < 18:
    print("Consult a dietitian for an age-appropriate diet")
elif condition == "diabetes":
    print("Choose balanced meals with professional guidance")
elif bmi < 18.5:
    print("Recommendation: Balanced, nourishing meals")
elif bmi < 25:
    print("Recommendation: Maintain a balanced diet")
else:
    print("Consider personalized dietary guidance")

finish()
