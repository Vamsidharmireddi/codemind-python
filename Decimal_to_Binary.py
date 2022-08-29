n=int(input())
for i in range(0,n):
    b=int(input())
    a=[]
    while b>0:
        rem=b%2
        a.append(rem)
        b=b//2
    for i in range(len(a)-1,-1,-1):
        print(a[i],end='')
    print("")