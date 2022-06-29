n,k=map(int,input().split())
a=list(map(int,input().split()))
x=0
for i in range(len(a)):
    c=0
    temp=abs(a[i])
    if temp==0:
        c=1
    while temp:
        d=temp%10
        c=c+1
        temp=temp//10
    if c==k:
        x=x+1
print(x)