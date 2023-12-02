res = 0
for i in open('input/day2.txt','r').read().split('\n'):
 a = i.split(": ")[1].split(";")
 r,g,b=0,0,0
 for j in a:
  for k in j.split(','):
   c=int(k.strip().split(" ")[0])
   if k.find("red")!=-1 and c>r:r=c
   if k.find("green")!=-1 and c>g:g=c
   if k.find("blue")!=-1 and c>b:b=c
 res += r*g*b
print(res) # 70768