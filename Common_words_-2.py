a=input()
b=input()
#print(a)
#print(b)
c=a.split()
d=b.split()
s=0
for i in c:
    if i in d and d.count(i)==1 and c.count(i)==1:
        s=s+1
        #print(i,end=' ')
print(s)
    