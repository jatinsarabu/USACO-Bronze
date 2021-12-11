capacities = []
milk = []
with open ('mixmilk.in', 'r') as f: 
    for _ in range(3): 
        line = f.readline().split()
        capacities.append(int(line[0]))
        milk.append(int(line[1]))

for count in range(0,100): 
    milk[(count +1)%3] += milk[(count)%3] 
    milk[count%3] = 0 
    if milk[(count+1)%3] > capacities[(count +1)%3]:
        milk[(count)%3] += (milk[(count+1)%3] - capacities[(count+1)%3])
        milk[(count+1)%3] -= (milk[(count+1)%3] - capacities[(count+1)%3])
with open('mixmilk.out','w')as f: 
    for bucket in milk: 
        f.write((str(bucket)+"\n"))
