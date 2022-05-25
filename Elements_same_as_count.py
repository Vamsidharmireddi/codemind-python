n=int(input())
a=list(map(int,input().split()))
k=0
for i in range(0,n):
    c=1
    for j in range(0,n):
        if a[i]==a[j] and i!=j:
            c=c+1
            a[j]=0
    if a[i]==c:
        k=k+1
        print(a[i],end=' ')
if k==0:
    print('-1')

        