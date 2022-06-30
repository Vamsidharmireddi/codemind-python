n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    r=0
    temp=i
    while i>0:
        d=i%10
        r=r*10+d
        i=i//10
    if temp==r:
        c=c+1
print(c)
    