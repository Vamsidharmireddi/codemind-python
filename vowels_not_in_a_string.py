n=input()
v={'a','e','i','o','u'}
c=[]
for i in v:
    if i not in n:
        c.append(i)
if len(c)!=0:
    b=sorted(c)
    print(*b)
else:
    print(0)