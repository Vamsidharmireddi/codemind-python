a=int(input())
b=int(input())
for i in range(a,b+1):
    k=0
    c=0
    temp=i
    while i>0:
        d=i%10
        k=k+1
        if d!=0:
            if temp%d==0:
                c=c+1
        i=i//10
    if k==c:
        print(temp,end=' ')