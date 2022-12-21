n=input()
a=n.split()
m=0
for i in a:
    if len(i)>m:
        m=len(i)
print(m)