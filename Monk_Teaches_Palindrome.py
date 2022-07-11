n=int(input())
for i in range(0,n):
    n=input()
    k=n[::-1]
    z=len(n)
    if k==n:
        if z%2==0:
            print('YES EVEN')
        else:
            print('YES ODD')
    else:
        print('NO')