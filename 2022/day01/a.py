lines = [l.strip() for l in open("../../input.txt").readlines()]

s, c = 0, 0
for line in lines:
  if not line:
    if c > s:
      s = c
    c = 0
  else:
    c += int(line)

print(s)


