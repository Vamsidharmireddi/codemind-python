n=int(input())
a=list(map(int,input().split()))
k=0
s=0
for i in range(0,n):
    for j in range(0,n):
        if a[i]==a[j] and i!=j:
            a[j]=0
    else:
        s=s+a[i]
print(s)


        