import copy
from pprint import pprint

# Kreiranje dict-a
d1 = dict()

a = [1, 2, 3]

d1["a"] = a

# Kopiranje
d2 = d1
dShallow = copy.copy(d1)
dDeep = copy.deepcopy(d1)

print(id(d1), d1, "d1")
print(id(d2), d2, "d2")
print()
print(id(dShallow), dShallow, "dShallow")
print()
print(id(dDeep), dDeep, "dDeep")
input()

# Dodavanje kljuca
d2["d2"] = 1
dShallow["dShallow"] = 1
dDeep["dDeep"] = 1

print('\n')
print(d1, "d1")
print(d2, "d2")
print()
print(dShallow, "dShallow")
print()
print(dDeep, "dDeep")
input()

# Izmena vrednosti
d2["a"].append("d2")
dShallow["a"].append("dShallow")
dDeep["a"].append("dDeep")

print('\n')
print(d1, "d1")
print(d2, "d2")
print(dShallow, "dShallow")
print()
print(dDeep, "dDeep")