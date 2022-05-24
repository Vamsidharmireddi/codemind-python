n=int(input())
a=list(map(int,input().split()))
c=0
s=0
for i in range(0,len(a)):
    if a[i]!=1:
        for j in range(2,int(a[i]**0.5)+1):
            if(a[i]%j==0):
                break
        else:
            c=c+1
            s=s+a[i]
avg=s/c
print("{:.2f}".format(avg))