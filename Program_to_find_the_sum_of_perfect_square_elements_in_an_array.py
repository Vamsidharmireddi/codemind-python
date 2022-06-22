n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    #print(a)
    for j in range(0,i+1):
        if j*j==i:
            #print(i,end=' ')
            s=s+i
print(s)