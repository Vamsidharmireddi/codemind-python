n=int(input())
a=list(map(int,input().split()))
k,p=map(int,input().split())
c=0
for i in range(0,len(a)):
    if a[i]<k or a[i]>p:
        print(a[i],end=' ')
        c=c+1
if c==0:
    print('-1')