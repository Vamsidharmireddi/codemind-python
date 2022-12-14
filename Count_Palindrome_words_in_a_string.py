a=input()
b=a.lower()
x=b.split()
c=0
for i in x:
    if i==i[::-1]:
        c=c+1
print(c)