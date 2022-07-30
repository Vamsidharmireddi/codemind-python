n=input()
d=[]
for i in n:
    if i.islower():
        if n.count(i)==1:
            d.append(i)
k=sorted(d)
for i in k:
    print(i,end='')