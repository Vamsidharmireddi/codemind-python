n=int(input())
a=list(map(int,input().split()))
d=[]
for i in range(0,len(a)):
    if a[i] not in d:
        d.append(a[i])
print(*d)