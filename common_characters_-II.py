a=input()
b=input()
x=a.lower()
y=b.lower()
s=""
for i in x:
    if i in y:
        s=s+i
p=sorted(set(s))
c=0
for i in p:
    if i!=' ':
        c=c+1
print(c)
        