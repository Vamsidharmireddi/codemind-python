x=input()
y=input()
a=x.lower()
b=y.lower()
#print(a)
#print(b)
c=a.split()
d=b.split()
s=0
for i in c:
    if i in d :
        s=s+1
        #print(i,end=' ')
print(s)
    