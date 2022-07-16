n=int(input())
a=list(map(int,input().split()))
k=0
c=0
for i in range(0,len(a)//2):
    k=k+a[i]
for i in range(len(a)//2,len(a)):
    c=c+a[i]
print(k)
print(c)