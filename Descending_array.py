n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,len(a)-1):
    if a[i]>a[i+1]:
        c=c+1
    else:
        print('no')
        break
if c==len(a)-1:
    print('yes')
    