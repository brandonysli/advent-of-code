lines = [l.strip() for l in open("../../input.txt").readlines()]

s = 0
for line in lines:
  f = set(list(line[:len(line)//2]))
  b = set(list(line[len(line)//2:]))
  x = f.intersection(b)
  elem = x.pop()
  if elem.islower():
    s += ord(elem) - ord('a') + 1
  else: 
    s += ord(elem) - ord('A') + 27
  
print(s)
      
          