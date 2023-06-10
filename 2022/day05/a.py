from collections import deque
lines = [l.strip() for l in open("../../input.txt").readlines()]

s = ''
stacks = []
for line in lines:
  if line[0].isdigit():
    num_of_stacks = int(line.split(' ')[-1])
    stacks = [deque() for i in range(num_of_stacks)]
    break

for line in lines: 
  if line == '':
    break
  idx = int((num_of_stacks * 4 - len(line)) / 4)
  for i in range(1, len(line), 4):
    if line[i].isalpha():
      stacks[idx].appendleft(line[i])
    idx += 1

for line in lines:
  if line == '' or not line[0].isalpha():
    continue
  preconfig = line.split(' ')
  config = [preconfig[1], preconfig[3], preconfig[5]]
  for i in range(int(config[0])):
    stacks[int(config[2]) - 1].append(stacks[int(config[1]) - 1].pop())

for stack in stacks:
  s += stack[-1]

print(s)

  
  
  