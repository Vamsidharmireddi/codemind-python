n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    r=0
    while i>0:
        d=i%10
        r=r+d
        i=i//10
    c=c+r
print(c)
    