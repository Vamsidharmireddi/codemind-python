n=int(input())
a=list(map(int,input().split()))
#print(a)
k=int(input())
#print(k)
c=0
for i in a:
    if k==i:
        c=c+1
print(c)