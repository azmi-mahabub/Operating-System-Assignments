req_s = input("Enter numbers: ")
req_s = list(map(int, req_s.split()))
head = int(input("Enter head: "))
total = 0
list1 = []
sum = 0
i=1
total = abs(req_s[0]-head)
list1.append(total)
sum+=total

while (len(req_s)>i):
  if (req_s[i] == head):
    total1 = abs(req_s[i+1]-req_s[i-1])
    list1.append(total1)
    sum+=total1
    i = i+1
  elif (req_s[i-1] == head):
    i = i+1
  else:
    total1 = abs(req_s[i]-req_s[i-1])
    list1.append(total1)
    sum+=total1
    i=i+1

print(f"Original List = {req_s}")
print(list1)
print(sum)