a=input()
b=a.lower()
k=b.split()
c=0
for i in k:
    if i==i[::-1]:
        c=c+1
print(c)