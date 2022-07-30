a=input()
k=0
for i in range(0,len(a)):
    c=0
    for j in range(0,len(a)):
        if i!=j:
            if a[i]==a[j]:
                c=1
                break
    if c==0:
        print(i)
        k=k+1
        break
if k==0:
    print('-1')