a=list(map(int,input().split()))
s=0
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if i!=j:
            if s<(a[i]-1)*(a[j]-1):
                s=(a[i]-1)*(a[j]-1)
print(s)