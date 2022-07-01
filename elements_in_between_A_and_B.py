n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
k=0
for i in range(0,len(a)):
    if a[i]>=b and a[i]<=c:
        print(a[i],end=' ')
        k=k+1
if k==0:
    print('-1')

    