n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    s=0
    temp=a[i]
    while a[i]>0:
        d=a[i]%10
        s=s*10+d
        a[i]=a[i]//10
    if s==temp:
        c=c+1
print(c)