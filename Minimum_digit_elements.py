n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(0,len(a)):
    c=0
    temp=a[i]
    while temp>0:
        d=temp%10
        c=c+1
        temp=temp//10
    b.append(c)
k=min(b)
x=0
for i in range(0,len(a)):
    c=0
    temp=a[i]
    while temp>0:
        d=temp%10
        c=c+1
        temp=temp//10
    if c==k:
        x=x+1
print(x)

    
    