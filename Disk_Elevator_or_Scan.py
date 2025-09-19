req_s = [14, 20, 29, 40, 50, 110]
head = 29
direction = input("Enter the direction: ")
direction = direction.lower()
sum = 0

req_s.sort(key=lambda x: x)

if direction == "left":
  for i in range(len(req_s)):
    if req_s[i] == head:
      for j in range(i, 0, -1):
        sum += abs(req_s[j] - req_s[j-1])
        print(sum)
      sum+=abs(req_s[0]-req_s[i+1])
      print(sum)

      for j in range(i+1, len(req_s)-1):
        sum += abs(req_s[j] - req_s[j+1])
        print(sum)

elif direction == "right":
  for i in range(len(req_s)):
    if req_s[i] == head:
      for j in range(i, len(req_s)-1):
        sum += abs(req_s[j] - req_s[j+1])
        print(sum) 
      sum+=abs(req_s[-1]-req_s[i-1])
      print(sum)
      for j in range(i-1, 0, -1):
        sum += abs(req_s[j] - req_s[j-1])
        print(sum)
      
