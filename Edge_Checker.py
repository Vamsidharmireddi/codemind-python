x,y=map(int,input().split())
if y==x+1 or x==y+1:
    print('Yes')
elif x==10 and y==1:
    print('Yes')
elif x==1 and y==10:
    print('Yes')
else:
    print('No')