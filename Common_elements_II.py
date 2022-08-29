a,b=map(int,input().split())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
c=[]
for i in p:
    if i not in q:
        c.append(i)
for i in q:
    if i not in p:
        c.append(i)
print(*c)