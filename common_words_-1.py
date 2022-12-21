s1=input().lower()
s2=input().lower()
a=s1.split()
b=s2.split()
c=0
for i in a:
    if i in b:
        c=c+1
print(c)