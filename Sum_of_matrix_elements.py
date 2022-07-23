R=int(input())
C=int(input())
s=0
for i in range(R):
    k=list(map(int,input().split()))
    s=s+sum(k)
print(s)