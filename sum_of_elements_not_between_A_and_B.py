n=int(input())
a=list(map(int,input().split()))
k,p=map(int,input().split())
c=0
for i in range(0,len(a)):
    if a[i]<k or a[i]>p:
        c=c+a[i]
print(c)