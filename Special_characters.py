n=input()
d={'1','2','3','4','5','6','7','8','9','0'}
c=0
a=[]
b=[]
r=[]
for i in n:
    if i.isalpha():
        continue
    elif i in d:
        k=int(i)
        r.append(k)
        if k%2==0:
            a.append(k)
        else:
            b.append(k)
    else:
        c=c+1
p=len(a)
q=len(b)
if p>q:
    x=q
else:
    x=p
if c%2==0:
    for i in range(0,x):
        print(a[i],end='')
        print(b[i],end='')
else:
    for i in range(0,x):
        print(b[i],end='')
        print(a[i],end='')
if p>q:
    for i in range(q,p):
        print(a[i],end='')
else:
    for i in range(p,q):
        print(b[i],end='')