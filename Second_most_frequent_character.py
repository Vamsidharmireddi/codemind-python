a=input()
b=set(a)
c=0
d=[]
for i in b:
    c=a.count(i)
    d.append(c)
k=max(d)
z=set(d)
m=0
for i in d:
    if i!=k:
        if i>m:
            m=i
for i in b:
    if a.count(i)==m:
        print(i)
        break
if len(z)==1:
    print('-1')