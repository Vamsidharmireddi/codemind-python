n1=int(input())
a=list(map(int,input().split()))
n2=int(input())
b=list(map(int,input().split()))
k=int(input())
c=0
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if i==j:
            if k>=a[i] and k<=b[j]:
                c=c+1
print(c)
        
        