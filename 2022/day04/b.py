lines = [l.strip() for l in open("../../input.txt").readlines()]

s = 0
for line in lines:
  assignments = line.split(',')
  e1 = assignments[0].split('-')
  e2 = assignments[1].split('-')

  if int(e1[0]) >= int(e2[0]) and int(e1[0]) <= int(e2[1]):
    s += 1
  elif int(e2[0]) <= int(e1[1]) and int(e2[0]) >= int(e1[0]):
    s += 1

print(s)