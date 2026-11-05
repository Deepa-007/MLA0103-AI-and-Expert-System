
from lab_utils import start, ask, finish

start("program27_output.txt")

sentence = ask("Enter a sentence: ").lower()
vowels = "aeiou"
found = []

for ch in sentence:
    if ch in vowels:
        found.append(ch)

print("Vowels:", found)
print("Total vowels:", len(found))

finish()
