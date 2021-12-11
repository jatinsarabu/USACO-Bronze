with open ("square.in") as f: 
  a = [int(x) for x in f.readline().split()]
  b = [int(x) for x in f.readline().split()]
  x = []
  y = []
  x.append(a[0])
  x.append(a[2])
  x.append(b[0])
  x.append(b[2])
  y.append(a[1])
  y.append(a[3])
  y.append(b[1])
  y.append(b[3])
difference = max(max(x)-min(x),max(y)-min(y))
with open("square.out","w") as f: 
  f.write(str(difference**2))
