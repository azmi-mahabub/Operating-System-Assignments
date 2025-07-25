x = [
    {"pid": 'P1', "arrival": 0, "burst": 3}, {"pid": 'P2', "arrival": 1, "burst": 2},
    {"pid": 'P3', "arrival": 2, "burst": 1}, {"pid": 'P4', "arrival": 3, "burst": 4}
]
x.sort(key=lambda x: x["arrival"])
total_TAT = 0
total_WT = 0
total =0
CT = []
TAT = []
WT = []
for i in x:
  total += i['burst']
  CT.append(total)
  TAT.append(total - i['arrival'])
  WT.append((total - i['arrival'])-i['burst'])

for i in range(len(x)):
  total_TAT += TAT[i]
  total_WT += WT[i]
print('Average of Turn Around Time = ', total_TAT/len(x))
print('Average of Waiting Time = ', total_WT/len(x))

for k in range(len(x)):
    x[k]['CT'] = CT[k]
    x[k]['TAT'] = TAT[k]
    x[k]['WT'] = WT[k]

print(x)