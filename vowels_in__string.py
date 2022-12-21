a=input()
v={'a','e','i','o','u','A','E','I','O','U'}
c=[]
for i in a:
    if i in v:
        c.append(i)
for i in range(0,len(c)):
    for j in range(0,len(c)):
        if i!=j and c[i]==c[j]:
            c[j]=0
    if c[i]!=0:
        print(c[i],end=' ')