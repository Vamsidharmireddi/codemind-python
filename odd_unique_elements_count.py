n=int(input())
a=list(map(int,input().split()))
k=0
for i in range(0,n):
    for j in range(0,n):
        if a[i]==a[j] and i!=j:
            a[j]=0
    if a[i]%2==1:
        k=k+1
        #print(a[i],end=' ')
print(k)
        