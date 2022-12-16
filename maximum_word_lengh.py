n=input()
a=n.split()
c=0
for i in a:
    if len(i)>c:
        c=len(i)
print(c)