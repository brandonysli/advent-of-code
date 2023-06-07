lines = [l.strip() for l in open("../../input.txt").readlines()]

s = 0
for line in lines:
  me = line[2]
  op = line[0]
  if me == 'X':
    if op == 'A':
      s += 3
    elif op == 'B':
      s += 1
    else:
      s += 2
  elif me == 'Y':
    s += 3
    if op == 'A':
      s += 1
    elif op == 'B':
      s += 2
    else:
      s += 3
  else:
    s += 6
    if op == 'A':
      s += 2
    elif op == 'B':
      s += 3
    else:
      s += 1

print(s)