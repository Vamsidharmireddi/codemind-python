n=int(input())
a=list(map(int,input().split()))
s=[]
b=[]
for i in a:
    if i%2==1:
        s.append(i)
    else:
        b.append(i)
k=s+b
for i in k:
    print(i,end=' ')