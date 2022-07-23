x,y=map(int,input().split())
a=x+2*y
if a%2==0:
    if x%2==0 and y%2==0:
        print('YES')
    elif x==0 and y%2!=0:
        print('NO')
    elif x%2==0 and 2*y%2==0:
        print('YES')
else:
    print('NO')
    