n=int(input())
a=list(map(int,input().split()))
c=0
k=0
for i in range(0,len(a)):
    if a[i]%2==0:
        c=c+a[i]
    else:
        k=k+a[i]
print(abs(c-k))