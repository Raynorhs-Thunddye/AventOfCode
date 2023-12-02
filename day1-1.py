import re
r=sum(int(i[re.search('[0-9]', i).span()[0]]+i[len(i)-re.search('[0-9]',i[::-1]).span()[0]-1]) for i in open('input/day1.txt','r').read().split('\n'))
print(r) # 55834