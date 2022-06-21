n=int(input())
a=[]
for i in range(0,n):
    k=int(input())
    a.append(k)
c=int(input())
bil=0
for i in a:
    if i<=c:
        bil=bil+1
    else:
        bil=bil+2
print(bil)