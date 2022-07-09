n=int(input())
a=list(map(int,input().split()))
k,p=map(int,input().split())
c=0
m=[]
for i in range(0,len(a)):
    if a[i]<k or a[i]>p:
        c=c+1
        m.append(a[i])
if c==0:
    print('-1')
else:
    print(max(m))