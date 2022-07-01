n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(0,len(a)):
    c=1
    for j in range(0,len(a)):
        if i!=j:
            if a[i]==a[j]:
                c=c+1
                a[j]=0
    if a[i]!=0:
        print(a[i],c,end=' ')