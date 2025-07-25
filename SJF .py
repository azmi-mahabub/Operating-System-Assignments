x = [
    {"pid": 'P1', "arrival": 0, "burst": 3}, {"pid": 'P2', "arrival": 1, "burst": 2}, {"pid": 'P3', "arrival": 2, "burst": 1},
    {"pid": 'P4', "arrival": 3, "burst": 4}, {"pid": 'P5', "arrival": 0, "burst": 2}
]
n = len(x)
total_TAT =0
total_WT = 0
sum = 0
i=0
lis = []
CT = []
TAT = []
WT = []

while(len(lis)<n):
  x.sort(key=lambda x: (x["arrival"], x["burst"]))
  lis2 = []
  for j in x:
    if j['arrival']<=sum:
      lis2.append(j)
    lis2.sort(key=lambda x: x["burst"])

  sum += lis2[i]['burst']
  CT.append(sum)
  TAT.append(sum-lis2[i]['arrival'])
  WT.append(sum-lis2[i]['arrival'] - lis2[i]['burst'])
  x.remove(lis2[i])
  lis.append(lis2[i])

for j in range(len(lis)):
  total_TAT += TAT[j]
  total_WT += WT[j]
print('Average of Turn Around Time = ', total_TAT/n)
print('Average of Waiting Time = ', total_WT/n)

for k in range(len(lis)):
    lis[k]['CT'] = CT[k]
    lis[k]['TAT'] = TAT[k]
    lis[k]['WT'] = WT[k]

print(lis)