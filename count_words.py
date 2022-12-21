n=input()
a=n.split()
v={'a','e','i','o','u','A','E','I','O','U'}
s=0
for c in a:
    f=0
    k=len(c)
    for j in range(0,len(c)):
        if c[j].isalpha():
            if c[0] in v and c[k-1] not in v:
                f=f+1
    if f!=0:
        s=s+1
print(s)