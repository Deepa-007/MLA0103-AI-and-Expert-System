
from lab_utils import start, ask, finish

start("program17_output.txt")

fever = ask("Fever? (yes/no): ").lower()
cough = ask("Cough? (yes/no): ").lower()
sneezing = ask("Sneezing? (yes/no): ").lower()

if fever == "yes" and cough == "yes":
    print("Possible respiratory infection")
elif sneezing == "yes" and fever == "no":
    print("Possible allergy or cold")
else:
    print("Insufficient information")

print("This is an educational system, not a medical diagnosis.")
finish()
