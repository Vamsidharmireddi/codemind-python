n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
d=[]
e=[]
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if i!=j:
            if a[i]==a[j]:
                a[j]=0
    if a[i]!=0:
        d.append(a[i])
for i in range(0,len(b)):
    for j in range(0,len(b)):
        if i!=j:
            if b[i]==b[j]:
                b[j]=0
    if b[i]!=0:
        e.append(b[i])
for i in d:
    if i in e:
        print(i,end=' ')