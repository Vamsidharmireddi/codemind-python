n=int(input())
n1=0
n2=1
c=0
for i in range(1,n+1):
    n3=n1+n2
    if n3==n:
        c=c+1
        print('True')
        break
    n1=n2
    n2=n3
if c==0:
    print('False')