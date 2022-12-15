n=int(input())
a=[]
b=[]
for i in range(0,n):
    p=int(input())
    a.append(p)
for i in range(0,n):
    h=int(input())
    b.append(h)
count=0
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if a[i]<=b[j]:
            b[j]=0
            break
    else:
        count=count+1
print(count)