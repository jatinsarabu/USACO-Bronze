#Problem Link: http://usaco.org/index.php?page=viewproblem2&cpid=687
names = []
amounts = []
with open("notlast.in") as f: 
  N = int(f.readline())
  for i in range(N):
    line = f.readline().split()
    if line[0] not in names:
      names.append(str(line[0]))
      amounts.append(int(line[1]))
    else: 
      amounts[names.index(line[0])] += int(line[1])
with open("notlast.out","w")as f: 
  if len(names) == 1: 
    f.write(str(names[0])) 
    f.close()
    quit()
  a = sorted(amounts)
  res = []
  [res.append(x) for x in a if x not in res]
  if len(res) == 1: 
    f.write("Tie")
    f.close()
    quit()
  dc = res[1]
  f.write(str(names[amounts.index(dc)])+"\n")
