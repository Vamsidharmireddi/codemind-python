def is_self(n):
    temp=n
    c=0
    k=0
    while n>0:
        d=n%10
        c=c+1
        if d!=0:
            if temp%d==0:
                k=k+1
        n=n//10
    if c==k:
        return 1
    else:
        return 0
a=int(input())
b=int(input())
for i in range(a,b+1):
    if is_self(i):
        print(i,end=' ')