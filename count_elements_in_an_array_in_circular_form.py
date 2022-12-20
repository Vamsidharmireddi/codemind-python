n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,len(a)):
    if i==0:
        if (a[n-1]%2==0 and a[1]%2==1) or (a[n-1]%2==1 and a[1]%2==0):
            c=c+1
    elif i==n-1:
        if (a[n-2]%2==0 and a[0]%2==1) or (a[n-2]%2==1 and a[0]%2==0):
            c=c+1
    else:
        if (a[i-1]%2==0 and a[i+1]%2==1) or (a[i-1]%2==1 and a[i+1]%2==0):
            c=c+1
print(c)