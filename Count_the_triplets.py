n=int(input())
for i in range(0,n):
    k=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
                d=a[i]+a[j]
                for p in range(0,len(a)):
                    if a[p]==d:
                        c=c+1
    if c==0:
        print('-1')
    else:
        print(c)