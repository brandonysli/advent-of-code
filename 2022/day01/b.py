lines = [l.strip() for l in open("../../input.txt").readlines()]

fst = snd = thd = 0
s = 0
for line in lines:
  if not line:
    if s > thd:
      temp = thd
      thd = s
      fst = snd
      snd = temp
    elif s > snd:
      fst = snd
      snd = s
    elif s > fst:
      fst = s
    s = 0
  else:
    s += int(line)

print(fst + snd + thd)