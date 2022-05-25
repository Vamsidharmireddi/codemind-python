n=int(input())
a=list(map(int,input().split()))
for i in range(0,len(a)):
    s=0
    while a[i]!=0:
        d=a[i]%10
        s=s*10+d
        a[i]=a[i]//10
    print(s,end=' ')
    