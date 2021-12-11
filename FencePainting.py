with open('paint.in','r')as f: 
  first_line = f.readline().split()
  second_line = f.readline().split()
  a = int(first_line[0])
  b = int(first_line[1])
  c = int(second_line[0])
  d = int(second_line[1])
total = (b-a)+(d-c)
intersection = max(min(b,d)-max(a,c),0)
union = total - intersection

with open('paint.out','w')as f: 
  f.write(str(union))
