#Problem Link: http://usaco.org/index.php?page=viewproblem2&cpid=664
letters = "abcdefghijklmnopqrstuvwxyz"
l = [0]*26
b = [0]*26
final = [0]*26
words = []
with open("blocks.in","r") as f: 
  N = int(f.readline())
  for i in range(N): 
    l = [0]*26
    b = [0]*26
    w = f.readline().split()
    for ch in w[0]: 
      l[letters.index(ch)] +=1
    for ch in w[1]: 
      b[letters.index(ch)] +=1
    for i in range(26): 
      final[i] += max(b[i],l[i])
with open("blocks.out","w")as f: 
  for fi in final: 
    f.write(str(fi))
    f.write(str("\n"))
