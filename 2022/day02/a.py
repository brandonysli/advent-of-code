lines = [l.strip() for l in open("../../input.txt").readlines()]

s = 0
for line in lines:
  op =  ord(line[0]) - ord('A') + 1
  me = ord(line[2]) - ord('A')
  s += me - 22
  if op == 1 and me == 24 or op == 2 and me == 25 or op == 3 and me == 23:
    s += 6
  elif op == 1 and me == 23 or op == 2 and me == 24 or op == 3 and me == 25:
    s += 3

print(s)
  