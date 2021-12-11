moves = []
with open ("shell.in","r")as f: 
  N = f.readline()
  for i in range(int(N)): 
    moves.append([int(x) for x in f.readline().split()])
counters = []
for pebble in range(3):
  cones = [1,2,3]
  counter = 0
  for move in moves: 
    a = cones.index(move[0])
    b = cones.index(move[1])
    g = move[2]
    cones[a],cones[b] = cones[b],cones[a]
    if cones.index(g) == pebble: 
      counter +=1
  counters.append(counter)
with open("shell.out","w")as f: 
  f.write(str(max(counters)))
