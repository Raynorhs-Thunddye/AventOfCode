import re
m={'one': 1,'two': 2,'three': 3,'four': 4,'five': 5,'six': 6,'seven': 7,'eight': 8,'nine': 9}
p,q='[0-9]|' + '|'.join(list(m.keys())),'[0-9]|' + '|'.join(list(map(lambda x: x[::-1], list(m.keys()))))
r=0
for i in open('input/day1.txt','r').read().split('\n'):
 a=re.search(p, i).span()
 c=re.search(q, i[::-1]).span()
 r+=int(str(m[i[a[0]:a[1]]] if a[1]-a[0]!=1 else i[a[0]:a[1]])+str(m[i[len(i)-c[1]:len(i)-c[0]]] if c[1]-c[0]!=1 else i[len(i)-c[0]-1]))
print(r) # 53221