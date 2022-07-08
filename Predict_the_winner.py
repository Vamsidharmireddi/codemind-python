n=int(input())
a=list(map(int,input().split()))
s=0
k=0
if len(a)%2==0:
    c=len(a)//2
else:
    c=len(a)//2+1
for i in range(0,c):
    s=s+a[i]
for i in range(c,len(a)):
    k=k+a[i]
if (abs(s-k))%4==0:
    print('X')
else:
    print('Y')