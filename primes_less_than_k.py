n=int(input())
a=list(map(int,input().split()))
d=int(input())
c=0
for i in range(0,len(a)):
    if a[i]<=d:
        if a[i]==1:
            c=0
        else:
            for j in range(2,int(a[i]**0.5)+1):
                if(a[i]%j==0):
                    break
            else:
                c=c+1
print(c)