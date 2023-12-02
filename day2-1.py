res=0
for i in open('input/day2.txt','r').read().split('\n'):
 a = i.split(": ")[1].split(";")
 r,g,b=0,0,0
 for j in a:
  for k in j.split(','):
   c=int(k.strip().split(" ")[0])
   if k.find("red")!=-1 and c>r:r=c
   if k.find("green")!=-1 and c>g:g=c
   if k.find("blue")!=-1 and c>b:b=c
 if r<=12 and g<=13 and b<=14:res+=int(i.split(":")[0].split(" ")[1])
print(res) # 2563