n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    c=1
    for j in range(0,n):
        if a[i]==a[j] and i!=j:
            c=c+1
            a[j]=0
    if a[i]!=0:
        print(a[i],c,end=' ')

        