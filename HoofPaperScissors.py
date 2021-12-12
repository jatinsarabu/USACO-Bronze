#Problem Link: http://usaco.org/index.php?page=viewproblem2&cpid=688
from itertools import permutations
total  = 0
def hps(f1,f2): 
  global total
  if f1 == f2: 
    return 
  elif f1 == "H" and f2 == "S": 
    total +=1
    return 
  elif f1 == "S" and f2 == "P": 
    print("win")
    total +=1 
    return 
  elif f1 == "P" and f2 == "H": 
    total +=1 
    return 
nums = []  
totals = [] 
with open("hps.in","r")as f: 
  N = int(f.readline())
  for i in range(N): 
    line = [int(x) for x in f.readline().split()]
    nums.append(line)
  for permutation in permutations("HPS"):
    total = 0
    for num in nums:
      hps(permutation[num[0]-1],permutation[num[1]-1])
    totals.append(total)
with open ("hps.out","w")as f: 
  f.write(str(max(totals)))
