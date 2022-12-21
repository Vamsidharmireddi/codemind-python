n=input()
a=n.split()
v={'a','e','i','o','u'}
m=0
for i in a:
    c=0
    for j in i:
        if j in v:
            c=c+1
    if c>m:
        m=c
print(m)