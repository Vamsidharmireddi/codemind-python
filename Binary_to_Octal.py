n=int(input())
for i in range(0,n):
    b=int(input())
    a=0
    i=0
    while b>0:
        rem=b%10
        a=a+rem*(2**i)
        b=b//10
        i=i+1
    s=[]
    while a>0:
        r=a%8
        s.append(r)
        a=a//8
    for i in range(len(s)-1,-1,-1):
        print(s[i],end='')
    print("")