def add(n):
    s=0
    while n>0:
        d=n%10
        s=s+d**2
        n=n//10
    if s>0 and s<9:
        return s
    else:
        return add(s)
n=int(input())
s=add(n)
if s==1 or s==7:
    print('True')
else:
    print('False')