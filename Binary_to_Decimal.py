n=int(input())
for i in range(0,n):
    b=input()
    a=b[::-1]
    s=0
    for i in range(0,len(a)):
        s=s+(2**i)*(int(a[i]))
    print(s)