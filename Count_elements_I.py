n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=set(a)
y=set(b)
c=0
s=0
for i in x:
    if i in y:
        c=c+1
print(c)
        
