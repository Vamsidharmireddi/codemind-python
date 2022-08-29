n=int(input())
for i in range(0,n):
    b=int(input())
    a=[]
    while b>0:
        rem=b%10
        a.append(rem)
        b=b//10
    s=0
    for i in range(0,len(a)):
        s=s+a[i]*(8**i)
    f=[]
    while s>0:
        rem=s%2
        f.append(rem)
        s=s//2
    for i in range(len(f)-1,-1,-1):
        print(f[i],end='')
    print("")