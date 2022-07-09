n=int(input())
a=list(map(int,input().split()))
k=a[::-1]
s=0
for i in range(0,len(k)):
    s=s+k[i]*(2**i)
print(s)  