from collections import deque
line = open("../../input.txt").readline()

res = 1
q = deque()
q.append(line[0])

while len(q) != len(set(q)) or len(q) < 3:
    if len(q) == 4:
        q.popleft()
    res += 1
    q.append(line[res])
    
print(res + 1)

  
    

