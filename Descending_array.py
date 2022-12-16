n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
if a==b[::-1]:
    print('yes')
else:
    print('no')