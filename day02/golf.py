# p1
h=d=0
for b in open('day2.txt'):x,y=b.split();z=int(y);a=len(x)-3;d+=z*a*(a<4);h+=z*(a>1)
print(h*d)

# p2
a=h=d=0
for b in open('day2.txt'):
 x,y=b.split();z=int(y)
 if'f'!=x[0]:a+=z*(len(x)-3)
 else:h+=z;d+=z*a
print(h*d)
