n=int(input())
a=list(map(int,input().split()))
k=0
for i in range(0,n):
    s=0
    while a[i]>0:
        d=a[i]%10
        s=s+d
        a[i]=a[i]//10
    k=k+s
print(k)