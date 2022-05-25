n=int(input())
a=list(map(int,input().split()))
k=int(input())
m=0
for i in range(0,n):
    c=1
    for j in range(0,n):
        if a[i]==a[j] and i!=j:
            c=c+1
            a[j]=0
    if k==c and a[i]!=0:
        m=m+1
        print(a[i],end=' ')
if m==0:
    print('-1')

        