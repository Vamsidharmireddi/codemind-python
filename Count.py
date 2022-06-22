n=int(input())
a=list(map(int,input().split()))
c=0
k=0
for i in a:
    if i%2==0:
        c=c+1
    else:
        k=k+1
print(c,k,end=' ')