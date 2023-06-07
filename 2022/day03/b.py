lines = [l.strip() for l in open("../../input.txt").readlines()]

s = 0
for i in range(0, len(lines), 3):
  fst = set(list(lines[i]))
  snd = set(list(lines[i + 1]))
  thd = set(list(lines[i + 2]))
  x1 = fst.intersection(snd)
  x = x1.intersection(thd)
  elem = x.pop()
  if elem.islower():
    s += ord(elem) - ord('a') + 1
  else: 
    s += ord(elem) - ord('A') + 27

print(s)