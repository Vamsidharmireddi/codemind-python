s=input()
s=s.lower()
k=set(s)
g=[]
for i in k:
    if i!=" ":
        g.append(i)
b=sorted(g)
for i in b:
    print(i,end='')