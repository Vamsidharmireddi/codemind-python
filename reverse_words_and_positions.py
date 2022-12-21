n=input()
a=n.split()
for i in range(len(a)-1,-1,-1):
    k=a[i]
    print(k[::-1],end=' ')