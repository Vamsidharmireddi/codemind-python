n=int(input())
a=list(map(int,input().split()))
for i in a:
    c=0
    k=abs(i)
    if k==0:
        c=1
    while k>0:
        d=k%10
        c=c+1
        k=k//10
    print(c,end=' ')