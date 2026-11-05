
from lab_utils import start, finish
from itertools import permutations

start("program11_output.txt")

letters = "SENDMORY"
found = False

for p in permutations(range(10), 8):
    d = dict(zip(letters, p))

    if d['S'] == 0 or d['M'] == 0:
        continue

    send = 1000*d['S'] + 100*d['E'] + 10*d['N'] + d['D']
    more = 1000*d['M'] + 100*d['O'] + 10*d['R'] + d['E']
    money = (10000*d['M'] + 1000*d['O'] + 100*d['N']
             + 10*d['E'] + d['Y'])

    if send + more == money:
        print("SEND =", send)
        print("MORE =", more)
        print("MONEY =", money)
        found = True
        break

if not found:
    print("Solution not found")

finish()
