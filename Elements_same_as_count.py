n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,len(a)):
    s=1
    for j in range(0,len(a)):
        if i!=j:
            if a[i]==a[j]:
                a[j]=0
                s=s+1
    if s==a[i] and a[i]!=0:
        print(a[i],end=' ')
        c=c+1
if c==0:
    print('-1')