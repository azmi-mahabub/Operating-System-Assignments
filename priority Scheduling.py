x = [
    {"pid": 1, "arrival": 0, "burst": 11, "priority": 2},
    {"pid": 2, "arrival": 5, "burst": 28, "priority": 0},
    {"pid": 3, "arrival": 12, "burst": 2, "priority": 3},
    {"pid": 4, "arrival": 2, "burst": 10, "priority": 1},
    {"pid": 5, "arrival": 9, "burst": 16, "priority": 4}
]
n = len(x)
sum = 0
lis = []
lis2 = []
i = 0
CT = []
WT = []
TAT = []

while(len(lis2) < n ):
    
  for j in x:
    if (j['arrival']<=sum):
      lis.append(j)
    lis.sort(key=lambda x: x['priority'])

  sum += lis[i]['burst']
  CT.append(sum)
  TAT.append(sum - lis[i]['arrival'])
  WT.append((sum - lis[i]['arrival']) - lis[i]['burst'])
  lis2.append(lis[i])

  x.remove(lis[i])
  lis.clear()

print(lis2, CT, TAT, WT)