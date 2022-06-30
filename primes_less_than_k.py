def is_prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=0
s=0
for i in range(0,len(a)):
    if a[i]<=k:
        if is_prime(a[i]):
            c=c+1
            s=s+a[i]
print(c)

        
