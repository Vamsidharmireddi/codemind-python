n=int(input())
for i in range(n-1,1,-1):
    r=0
    temp=i
    while i>0:
        d=i%10
        r=r*10+d
        i=i//10
    if temp==r:
        y=r
        break
dif1=abs(n-y)
k=n+1
while True:
    r1=0
    temp=k
    while temp>0:
        d1=temp%10
        r1=r1*10+d1
        temp=temp//10
    if k==r1:
        z=r1
        break
    k=k+1
dif2=abs(n-z)
if dif2==dif1:
    print(y,z,end=' ')
elif dif2>dif1:
    print(y)
else:
    print(z)