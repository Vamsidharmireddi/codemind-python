x=input()
y=input()
a=x.lower()
b=y.lower()
s=""
for i in a:
    if i not in b:
        s=s+i
for i in b:
    if i not in a:
        s=s+i        
p=s.lower()
m=sorted(set(p))
if len(m)==0:
    print(-1)
else:
    for i in m:
        if i!=' ':
            print(i,end='')