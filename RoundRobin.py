# Input processes
processes = [
    {"pid": 1, "arrival": 0, "burst": 5},
    {"pid": 2, "arrival": 1, "burst": 3},
    {"pid": 3, "arrival": 2, "burst": 1},
    {"pid": 4, "arrival": 3, "burst": 2},
    {"pid": 5, "arrival": 4, "burst": 3}
]

time_quantum = 2

for p in processes:
    p["remaining"] = p["burst"]
    p["ct"] = 0

processes.sort(key=lambda x: x["arrival"])

ready_q = []
time = 0
completed = 0
n = len(processes)

unarrived = processes.copy()

while completed < n:
    i = 0
    while i < len(unarrived):
        if unarrived[i]["arrival"] <= time:
            ready_q.append(unarrived.pop(i))
        else:
            i += 1

    if not ready_q:
        time += 1
        continue

    current = ready_q.pop(0)


    exec_time = min(time_quantum, current["remaining"])
    time += exec_time
    current["remaining"] -= exec_time


    i = 0
    while i < len(unarrived):
        if unarrived[i]["arrival"] <= time:
            ready_q.append(unarrived.pop(i))
        else:
            i += 1

    if current["remaining"] == 0:
        current["ct"] = time
        completed += 1
    else:
        ready_q.append(current)
sorted(processes, key=lambda x: x["pid"])
print("PID | AT | BT | CT | TAT | WT")
for p in processes:
    tat = p["ct"] - p["arrival"]
    wt = tat - p["burst"]
    print(f"{p['pid']:>3} | {p['arrival']:>2} | {p['burst']:>2} | {p['ct']:>2} | {tat:>3} | {wt:>2}")