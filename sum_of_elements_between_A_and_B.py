n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
s=0
for i in range(0,len(a)):
    if a[i]>=b and a[i]<=c:
        s=s+a[i]
print(s)
