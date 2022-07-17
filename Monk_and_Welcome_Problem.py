n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(0,len(a)):
    for j in range(0,len(b)):
        k=a[i]+b[i]
    print(a[i]+b[i],end=' ')