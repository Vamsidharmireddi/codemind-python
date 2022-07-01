n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if i!=j:
            if a[i]==a[j]:
                a[j]=0
    if a[i]%2==1:
            s=s+1
print(s)