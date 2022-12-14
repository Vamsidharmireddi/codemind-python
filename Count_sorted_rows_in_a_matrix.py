r,c=map(int,input().split())
c=0
for i in range(0,r):
    a=list(map(int,input().split()))
    k=sorted(a)
    if k==a or k[::-1]==a:
        c=c+1
print(c)