n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
m=[]
k=0
for i in range(0,len(a)):
    if a[i]>=b and a[i]<=c:
        m.append(a[i])
        k=k+1
if k==0:
    print('-1')
else:
    print(max(m))

    