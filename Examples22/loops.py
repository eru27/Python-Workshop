for i in range(0, 100, 3):
    print(i, end = ' ')
print()

j = 0
while j < 10:
    print('.', end = ' ')
    j += 1
print()

d = dict()
# d = {}

d['nula'] = 0
d['jedan'] = 1
d['dva'] = 2

for number in d:
    print(d[number], end = ' ')
print()

for key, val in d.items():
    print(key, ':', val)

d.keys()
d.values()
