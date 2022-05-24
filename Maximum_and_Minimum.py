n=int(input())
a=list(map(int,input().split()))
ma=0
k=0
for i in range(0,n):
    mi=a[0]
    c=0
    #print(a[i],end=' ')
    for j in range(0,n):
        if a[i]==a[j]:
            c=c+1
    if a[i]==c:
        k=k+1
        if ma<a[i]:
            ma=a[i]
    if a[i]==c:
        if mi>a[i]:
            mi=a[i]
if k==0:
    print('-1')
else:
    print(mi,ma,end=' ')
        