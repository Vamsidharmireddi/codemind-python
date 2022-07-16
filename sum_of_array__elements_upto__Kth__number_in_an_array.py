n=int(input())
a=list(map(int,input().split()))
k=int(input())
s=0
for i in range(0,len(a)):
    s=s+a[i]
    if a[i]==k:
        break
print(s)