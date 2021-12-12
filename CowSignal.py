#Problem Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=665
with open("cowsignal.in",'r')as f: 
  a = [int(x) for x in f.readline().split()]
  M,N,K = a[0],a[1],a[2]
  maze = []
  for i in range(M):
    line = f.readline().split()
    maze.append(line)
  maze2 = []
  for line in maze: 
    a = ""
    for c in line[0]: 
      for i in range(K):
        a+=c
    for i in range(K):
      maze2.append(a)
with open("cowsignal.out","w")as f: 
  for line in maze2: 
    f.write(str(line)+"\n")
