a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
p=set(x)
q=set(y)
c=0
for i in p:
    if i not in q:
        c=c+1
for i in q:
    if i not in p:
        c=c+1
print(c)