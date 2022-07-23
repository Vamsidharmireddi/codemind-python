m,n=map(int,input().split())
a=list(map(int,input().split()))
c=0
k=0
for i in range(0,len(a)):
    if a[i]<=n:
        c=c+1
    else:
        k=k+1
        if k==2:
            break
print(c)