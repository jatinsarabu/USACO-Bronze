with open ("billboard.in", "r")as f: 
  b1 = [int(x) for x in f.readline().split()]
  b2 = [int(x) for x in f.readline().split()]
  truck = [int(x) for x in f.readline().split()]

def area(bl_x, bl_y, tr_x, tr_y):
	length = tr_y - bl_y
	width = tr_x - bl_x
	return length * width

total = area(b1[0],b1[1],b1[2],b1[3])+area(b2[0],b2[1],b2[2],b2[3])
def inter_area(s1, s2):
	bl_a_x, bl_a_y, tr_a_x, tr_a_y = s1[0], s1[1], s1[2], s1[3]
	bl_b_x, bl_b_y, tr_b_x, tr_b_y = s2[0], s2[1], s2[2], s2[3]
	
	return (
		(min(tr_a_x, tr_b_x) - max(bl_a_x, bl_b_x))
		* (min(tr_a_y, tr_b_y) - max(bl_a_y, bl_b_y))
	)
total -= inter_area(b1,truck)
total -= inter_area(b2,truck)
with open("billboard.out","w")as f: 
  f.write(str(total))
